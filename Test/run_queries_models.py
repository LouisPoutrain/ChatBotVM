#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    requests = None


def load_env(root: Path) -> dict[str, str]:
    env = {}
    env_path = root / ".env"
    if not env_path.exists():
        return env
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def load_questions(query_file: Path) -> list[str]:
    questions: list[str] = []
    for raw_line in query_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # Keep only likely questions from query file
        if line.endswith("?") or line.endswith("？"):
            questions.append(line)
        elif len(line) > 10 and not line.startswith("#"):
            questions.append(line)
    return questions


def discover_models(base_url: str, headers: dict[str, str], exclude: set[str]) -> list[str]:
    if requests is None:
        raise RuntimeError("Module 'requests' non disponible. Installez requests ou spécifiez --models.")
    url = base_url.rstrip("/") + "/models"
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    models = []
    if isinstance(data, dict) and data.get("data"):
        for item in data.get("data", []):
            mid = item.get("id") or item.get("model")
            if mid and mid not in exclude:
                models.append(mid)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str) and item not in exclude:
                models.append(item)
    return sorted(list(dict.fromkeys(models)))


def find_project_root(script_dir: Path) -> tuple[Path, Path, Path]:
    cur = script_dir
    for _ in range(8):
        query_candidates = [
            cur / "Test" / "Queries" / "Query.txt",
            cur / "Test" / "Query.txt",
            cur / "Test" / "Queries" / "Query_Mix.txt",
        ]
        rag_candidates = [
            cur / "RAGilaas" / "RAGilaas.py",
            cur / "RAG" / "RAGilaas" / "RAGilaas.py",
        ]
        found_rag = next((r for r in rag_candidates if r.exists()), None)
        found_query = next((q for q in query_candidates if q.exists()), None)
        if found_rag:
            default_query = found_query or (cur / "Test" / "Queries" / "Query.txt")
            return cur, default_query, found_rag
        cur = cur.parent
    raise FileNotFoundError("Impossible de trouver la racine du projet (contenant RAGilaas/RAGilaas.py et Test/).")


def resolve_query_file(root: Path, query_arg: str | None, default_file: Path) -> Path:
    if not query_arg:
        return default_file
    p = Path(query_arg)
    if p.is_absolute() and p.exists():
        return p
    candidates = [
        root / p,
        root / "Test" / p,
        root / "Test" / "Queries" / p,
        root / "Test" / "Queries" / (p.name + ".txt" if not p.suffix else p.name),
    ]
    for c in candidates:
        if c.exists():
            return c
    return root / p


def update_latest_symlink(results_dir: Path, target_dir: Path) -> None:
    symlink_path = results_dir / "latest"
    try:
        if symlink_path.is_symlink() or symlink_path.exists():
            symlink_path.unlink()
        symlink_path.symlink_to(target_dir.name, target_is_directory=True)
    except Exception:
        pass


def run_ragilaas(
    python_exec: str,
    rag_script: Path,
    question: str,
    draft_model: str,
    answer_model: str,
    k: int,
    timeout: int,
    run_log_file: Path,
) -> dict[str, Any]:
    cmd = [
        python_exec,
        str(rag_script),
        "--question",
        question,
        "--draft-model",
        draft_model,
        "--answer-model",
        answer_model,
        "--k",
        str(k),
        "--log-file",
        str(run_log_file),
    ]
    t0 = time.time()
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        duration = round(time.time() - t0, 2)
        return {
            "returncode": proc.returncode,
            "duration_s": duration,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "cmd": cmd,
        }
    except subprocess.TimeoutExpired:
        duration = round(time.time() - t0, 2)
        return {
            "returncode": -1,
            "duration_s": duration,
            "error": f"Timeout expired after {timeout}s",
            "stdout": "",
            "stderr": "",
            "cmd": cmd,
        }


def extract_final_answer(stdout: str) -> str:
    match = re.search(r"Assistant\s*:\s*\n(?P<answer>.*?)(?:\n-{3,}\s*\n?|\Z)", stdout, flags=re.DOTALL)
    if match:
        return match.group("answer").strip()
    return stdout.strip()


def generate_models_summary_md(
    out_file: Path,
    query_name: str,
    models: list[str],
    results_by_model: dict[str, list[dict[str, Any]]],
    stats_by_model: dict[str, dict[str, Any]],
    k: int,
) -> None:
    lines = [
        "# 🤖 Synthèse de Comparaison Multi-Modèles",
        "",
        f"- **Date** : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Fichier de requêtes** : `{query_name}`",
        f"- **Nombre de chunks (k)** : {k}",
        f"- **Modèles testés** : {', '.join(f'`{m}`' for m in models)}",
        "",
        "---",
        "",
        "## 📊 Récapitulatif des Performances par Modèle",
        "",
        "| Modèle | Questions | Réussies | Échecs | Temps Moyen (s) | Temps Total (s) |",
        "|:---|:---:|:---:|:---:|:---:|:---:|",
    ]

    for model in models:
        st = stats_by_model.get(model, {})
        avg_d = f"{st.get('avg_duration_s', 0):.2f}s"
        tot_d = f"{st.get('total_duration_s', 0):.2f}s"
        succ = st.get("success_count", 0)
        fail = st.get("fail_count", 0)
        total = st.get("total_count", 0)
        lines.append(f"| **`{model}`** | {total} | {succ} | {fail} | {avg_d} | {tot_d} |")

    lines.extend([
        "",
        "---",
        "",
        "## 💬 Comparatif Détaillé des Réponses par Question",
        "",
    ])

    # Assumes all models processed the same questions
    ref_list = results_by_model.get(models[0], []) if models else []
    for idx, item in enumerate(ref_list):
        q = item.get("question", f"Question #{idx+1}")
        lines.append(f"### Q{idx+1} : {q}")
        lines.append("")
        for model in models:
            m_res = results_by_model.get(model, [])
            m_item = m_res[idx] if idx < len(m_res) else {}
            dur = m_item.get("duration_s", "?")
            ret = m_item.get("returncode", "?")
            ans = m_item.get("final_answer", "").strip() or "*(Aucune réponse ou erreur)*"
            err = m_item.get("error")
            status_emoji = "✅" if ret == 0 else "❌"

            lines.append(f"<details><summary><b>{status_emoji} Modèle : <code>{model}</code> ({dur}s)</b></summary>")
            lines.append("")
            if err:
                lines.append(f"> ⚠️ **Erreur** : {err}")
                lines.append("")
            lines.append(ans)
            lines.append("")
            lines.append("</details>")
            lines.append("")

    out_file.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Lance RAGilaas sur un ensemble de questions pour comparer plusieurs modèles")
    parser.add_argument("--query-file", type=str, default=None, help="Fichier des questions (par défaut: Query_Mix.txt ou Query.txt)")
    parser.add_argument("--output-dir", type=str, default=None, help="Dossier de sortie personnalisé (défaut: Results/YYYY-MM-DD_HH-MM_models_{query})")
    parser.add_argument("--models", type=str, default=None, help="Liste de modèles séparés par des virgules (ex: mistral-medium-latest,gemma-4-31b)")
    parser.add_argument("--exclude-models", type=str, default="llama-3.3-70b,gpt-oss-120b,llama-3.1-8b", help="Modèles à exclure de la détection API automatique")
    parser.add_argument("--k", type=int, default=6, help="Nombre de chunks pour RAGilaas (défaut: 6)")
    parser.add_argument("--timeout", type=int, default=600, help="Timeout par question en secondes (défaut: 600)")
    parser.add_argument("--python", type=str, default=sys.executable, help="Interpréteur Python à utiliser")
    parser.add_argument("--sleep-between", type=float, default=0.5, help="Pause entre 2 questions (défaut: 0.5s)")
    parser.add_argument("--max-models", type=int, default=0, help="Limiter le nombre de modèles (0 = tous)")
    parser.add_argument("--max-questions", type=int, default=0, help="Limiter le nombre de questions (0 = toutes)")
    parser.add_argument("--dry-run", action="store_true", help="N'exécute pas RAGilaas, prépare seulement le plan")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    try:
        root, default_query_file, rag_script = find_project_root(script_dir)
    except FileNotFoundError as exc:
        print(f"❌ {exc}")
        return

    query_file = resolve_query_file(root, args.query_file, default_query_file)
    if not query_file.exists():
        print(f"❌ Query file not found: {query_file}")
        return

    test_dir = root / "Test"
    results_base = test_dir / "Results"

    env = load_env(root)
    api_key = env.get("LLM_API_KEY") or os.getenv("LLM_API_KEY")
    base_url = (env.get("LLM_BASE_URL") or os.getenv("LLM_BASE_URL") or "https://llm.ilaas.fr/v1").rstrip("/")

    # Modèles
    if args.models:
        models = [m.strip() for m in args.models.split(",") if m.strip()]
        excluded: set[str] = set()
    else:
        if not api_key:
            print("❌ LLM_API_KEY manquante dans .env et variables d'environnement. Spécifiez --models manuellement.")
            return
        excluded = {m.strip() for m in args.exclude_models.split(",") if m.strip()}
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        print("🔍 Découverte des modèles depuis l'API...")
        try:
            models = discover_models(base_url, headers, excluded)
        except Exception as e:
            print(f"❌ Échec de découverte des modèles: {e}")
            return

    if not models:
        print("❌ Aucun modèle disponible.")
        return

    if args.max_models > 0:
        models = models[: args.max_models]

    print(f"📋 Modèles sélectionnés ({len(models)}) : {models}")

    questions = load_questions(query_file)
    if args.max_questions > 0:
        questions = questions[: args.max_questions]

    if not questions:
        print(f"❌ Aucune question trouvée dans {query_file}")
        return

    print(f"📝 {len(questions)} question(s) chargée(s) depuis {query_file.name}")

    if args.output_dir:
        out_dir = Path(args.output_dir) if Path(args.output_dir).is_absolute() else (test_dir / args.output_dir)
    else:
        now_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        out_dir = results_base / f"{now_str}_models_{query_file.stem}"
    out_dir.mkdir(parents=True, exist_ok=True)

    summary: dict[str, Any] = {
        "generated_at": datetime.datetime.now().isoformat(),
        "query_file": query_file.name,
        "excluded_models": sorted(excluded),
        "models": models,
        "question_count": len(questions),
        "runs": {},
        "rag_script": str(rag_script),
        "base_url": base_url,
        "dry_run": bool(args.dry_run),
    }

    results_by_model: dict[str, list[dict[str, Any]]] = {}
    stats_by_model: dict[str, dict[str, Any]] = {}

    for model_idx, model in enumerate(models, start=1):
        safe_model_name = model.replace("/", "_").replace(":", "_")
        print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"  [{model_idx}/{len(models)}] Exécution pour le modèle : {model}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        model_results = []
        model_log_file = out_dir / f"run_logs_{safe_model_name}.txt"
        total_duration = 0.0
        success_count = 0
        fail_count = 0

        for idx, q in enumerate(questions, start=1):
            print(f"  - Q{idx}/{len(questions)}: {q[:70]}...")
            if args.dry_run:
                entry = {
                    "question_index": idx,
                    "question": q,
                    "returncode": 0,
                    "duration_s": 0.01,
                    "stdout": "Dry run mock answer",
                    "stderr": "",
                    "final_answer": "Dry run mock answer",
                    "dry_run": True,
                }
            else:
                try:
                    res = run_ragilaas(
                        python_exec=args.python,
                        rag_script=rag_script,
                        question=q,
                        draft_model=model,
                        answer_model=model,
                        k=args.k,
                        timeout=args.timeout,
                        run_log_file=model_log_file,
                    )
                    ret = res.get("returncode", -1)
                    dur = res.get("duration_s", 0.0)
                    total_duration += dur
                    if ret == 0:
                        success_count += 1
                    else:
                        fail_count += 1

                    entry = {
                        "question_index": idx,
                        "question": q,
                        "returncode": ret,
                        "duration_s": dur,
                        "error": res.get("error"),
                        "stdout": res.get("stdout", ""),
                        "stderr": res.get("stderr", ""),
                        "final_answer": extract_final_answer(res.get("stdout", "")),
                        "cmd": res.get("cmd", []),
                    }
                    status_sym = "✅" if ret == 0 else "❌"
                    print(f"    {status_sym} terminé en {dur}s (code {ret})")
                except Exception as e:
                    fail_count += 1
                    entry = {
                        "question_index": idx,
                        "question": q,
                        "returncode": -1,
                        "duration_s": 0.0,
                        "error": str(e),
                        "final_answer": "",
                    }
                    print(f"    ❌ Exception: {e}")

            model_results.append(entry)
            time.sleep(args.sleep_between)

        results_by_model[model] = model_results
        stats_by_model[model] = {
            "total_count": len(model_results),
            "success_count": success_count,
            "fail_count": fail_count,
            "total_duration_s": total_duration,
            "avg_duration_s": (total_duration / len(model_results)) if model_results else 0.0,
        }

        out_file = out_dir / f"{safe_model_name}.json"
        out_file.write_text(json.dumps(model_results, ensure_ascii=False, indent=2), encoding="utf-8")
        summary["runs"][model] = {
            "questions": len(model_results),
            "stats": stats_by_model[model],
            "results_file": out_file.name,
            "rag_log_file": model_log_file.name,
        }

    # Sauvegarde du résumé JSON & Markdown
    summary_file = out_dir / "summary.json"
    summary_file.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    summary_md_file = out_dir / "summary.md"
    generate_models_summary_md(
        out_file=summary_md_file,
        query_name=query_file.name,
        models=models,
        results_by_model=results_by_model,
        stats_by_model=stats_by_model,
        k=args.k,
    )

    update_latest_symlink(results_base, out_dir)

    print(f"\n============================================================")
    print(f"✅ Comparaison terminée avec succès !")
    print(f"📁 Résultats enregistrés dans : {out_dir}")
    print(f"  - Synthèse Markdown   : {summary_md_file}")
    print(f"  - Synthèse JSON       : {summary_file}")
    print(f"============================================================")


if __name__ == "__main__":
    main()
