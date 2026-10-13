#!/usr/bin/env python3
"""Benchmark Multi-Modèles RAGilaas (10 Combinaisons)

Lance les combinaisons de modèles définies dans BenchComb.md sur un corpus de questions
avec un juge impartial (par défaut gpt-oss-120b).
Génère automatiquement les dossiers structurés dans Test/Results/ et le rapport
comparatif global conclusion_evaluations.md.
"""
from __future__ import annotations

import argparse
import datetime
import subprocess
import sys
import time
from pathlib import Path

COMBOS = [
    {"name": "01_baseline", "draft": "mistral-medium-latest", "answer": "mistral-medium-latest", "rac": "mistral-medium-latest", "desc": "Baseline de référence (tout Mistral Medium)"},
    {"name": "02_fast_draft_rac", "draft": "llama-3.1-8b", "answer": "mistral-medium-latest", "rac": "llama-3.1-8b", "desc": "Draft & RAC rapides 8B + réponse Mistral Medium"},
    {"name": "03_max_quality", "draft": "mistral-medium-latest", "answer": "mistral-small-4-119b", "rac": "mistral-small-4-119b", "desc": "Plafond max qualité (RAC 119B + réponse 119B)"},
    {"name": "04_meta_mono", "draft": "llama-3.1-8b", "answer": "llama-3.1-8b", "rac": "llama-3.1-8b", "desc": "Meta Mono 8B (vitesse max & ultra-léger de bout en bout)"},
    {"name": "05_qwen_reasoning_mono", "draft": "qwen-3.8-27b", "answer": "qwen-3.8-27b", "rac": "qwen-3.8-27b", "desc": "Qwen 27B Reasoning homogène (thinking sur RAC, HyDE et réponse)"},
    {"name": "06_google_mono", "draft": "gemma-4-31b", "answer": "gemma-4-31b", "rac": "gemma-4-31b", "desc": "Google Gemma 31B homogène sur l'ensemble du pipeline"},
    {"name": "07_qwen_instruct_mono", "draft": "qwen-3.6-35b-instruct", "answer": "qwen-3.6-35b-instruct", "rac": "qwen-3.6-35b-instruct", "desc": "Alibaba Qwen 35B Instruct homogène"},
    {"name": "08_economy_cross", "draft": "llama-3.1-8b", "answer": "qwen-3.6-35b-instruct", "rac": "llama-3.1-8b", "desc": "Economy Cross (Llama 8B Draft/RAC + Qwen 35B réponse)"},
    {"name": "09_premium_cross", "draft": "gemma-4-31b", "answer": "mistral-small-4-119b", "rac": "mistral-medium-latest", "desc": "Premium Cross (Gemma 31B Draft + RAC Medium + réponse 119B)"},
    {"name": "10_reasoning_rac", "draft": "mistral-medium-latest", "answer": "mistral-medium-latest", "rac": "qwen-3.8-27b", "desc": "RAC Reasoning 27B dédié + Draft & réponse Mistral Medium"},
]


def update_latest_symlink(results_dir: Path, target_dir: Path) -> None:
    symlink_path = results_dir / "latest"
    try:
        if symlink_path.is_symlink() or symlink_path.exists():
            symlink_path.unlink()
        symlink_path.symlink_to(target_dir.name, target_is_directory=True)
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(description="Benchmark Multi-Modèles RAGilaas (10 Combinaisons)")
    parser.add_argument("--query-file", type=str, default="Query_Mix.txt", help="Fichier de questions (défaut: Query_Mix.txt)")
    parser.add_argument("--judge-model", type=str, default="mistral-small-4-119b", help="Modèle Juge impartial (défaut: mistral-small-4-119b)")
    parser.add_argument("--rac-model", type=str, default=None, help="Forcer un modèle RAC spécifique pour toutes les combinaisons (optionnel)")
    parser.add_argument("--combos", nargs="+", default=["all"], help="Numéros ou noms des combinaisons à lancer (ex: 1 2 ou 01_baseline, défaut: all)")
    parser.add_argument("--max-questions", type=int, default=0, help="Limiter le nombre de questions par combo (0 = toutes)")
    parser.add_argument("--k", type=int, default=5, help="Nombre de chunks RAG (défaut: 5)")
    parser.add_argument("--timeout", type=int, default=600, help="Timeout par question en secondes (défaut: 600)")
    parser.add_argument("--output-dir", type=str, default=None, help="Dossier de sortie racine pour le benchmark")
    parser.add_argument("--python", type=str, default=sys.executable, help="Interpréteur Python à utiliser")
    args = parser.parse_args()

    test_dir = Path(__file__).resolve().parent
    runner_script = test_dir / "run_queries_ragilaas.py"
    summarize_script = test_dir / "summarize_evaluations.py"
    results_base = test_dir / "Results"

    # Sélection des combinaisons
    if "all" in args.combos:
        selected_combos = COMBOS
    else:
        selected_combos = []
        for c in args.combos:
            matched = False
            for idx, item in enumerate(COMBOS, start=1):
                if c == str(idx) or c.lower() in item["name"].lower():
                    selected_combos.append(item)
                    matched = True
                    break
            if not matched:
                print(f"⚠️ Combinaison inconnue : '{c}' (ignorée)")

    if not selected_combos:
        print("❌ Aucune combinaison sélectionnée. Arrêt.")
        return

    # Définition du dossier de sortie daté
    if args.output_dir:
        out_root = Path(args.output_dir) if Path(args.output_dir).is_absolute() else (test_dir / args.output_dir)
    else:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        query_stem = Path(args.query_file).stem
        out_root = results_base / f"{timestamp}_benchmark_{query_stem}"
    out_root.mkdir(parents=True, exist_ok=True)

    print("============================================================")
    print("  🚀 BENCHMARK MULTI-MODÈLES RAGilaas")
    print(f"  Fichier de requêtes : {args.query_file}")
    print(f"  Juge LLM           : {args.judge_model}")
    if args.rac_model:
        print(f"  Override RAC       : {args.rac_model}")
    print(f"  Combinaisons ({len(selected_combos)}/{len(COMBOS)}) : {[c['name'] for c in selected_combos]}")
    if args.max_questions > 0:
        print(f"  Limite questions   : {args.max_questions} par combinaison")
    print(f"  Dossier de sortie   : {out_root}")
    print("============================================================\n")

    start_bench_time = time.time()

    for idx, combo in enumerate(selected_combos, start=1):
        name = combo["name"]
        draft = combo["draft"]
        answer = combo["answer"]
        rac = args.rac_model if args.rac_model else combo.get("rac", "mistral-medium-latest")
        desc = combo["desc"]
        combo_out_dir = out_root / name

        print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"  [{idx}/{len(selected_combos)}] {name} : {desc}")
        print(f"  Draft: {draft} | Answer: {answer} | RAC: {rac} | Judge: {args.judge_model}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

        cmd = [
            args.python,
            str(runner_script),
            "--query-file",
            args.query_file,
            "--draft-model",
            draft,
            "--answer-model",
            answer,
            "--rac-model",
            rac,
            "--judge-model",
            args.judge_model,
            "--output-dir",
            str(combo_out_dir),
            "--k",
            str(args.k),
            "--timeout",
            str(args.timeout),
        ]
        if args.max_questions > 0:
            cmd.extend(["--max-questions", str(args.max_questions)])

        t0 = time.time()
        res = subprocess.run(cmd)
        dur = round(time.time() - t0, 2)
        if res.returncode == 0:
            print(f"\n  ✅ {name} terminé avec succès en {dur}s")
        else:
            print(f"\n  ⚠️ {name} s'est terminé avec le code {res.returncode} en {dur}s")

    # Génération du bilan comparatif global avec summarize_evaluations.py
    print("\n📊 Génération de la synthèse comparative globale...")
    subprocess.run([args.python, str(summarize_script), str(out_root)])

    update_latest_symlink(results_base, out_root)

    total_bench_duration = round(time.time() - start_bench_time, 2)
    minutes = int(total_bench_duration // 60)
    seconds = int(total_bench_duration % 60)

    print("\n============================================================")
    print("  🎉 BENCHMARK TERMINÉ AVEC SUCCÈS")
    print(f"  Durée totale : {minutes}m {seconds}s")
    print(f"  Rapport comparatif global : {out_root / 'conclusion_evaluations.md'}")
    print(f"  Dossier complet           : {out_root}")
    print("============================================================")


if __name__ == "__main__":
    main()
