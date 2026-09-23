#!/usr/bin/env python3
"""
Batch runner to send questions from Query*.txt to RAGilaas.py and collect logs.

Usage:
    python run_queries_ragilaas.py

It writes one log file and one JSON file per query source.
"""
from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
import traceback
import os
from pathlib import Path
import re
import tempfile
import time

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://llm.ilaas.fr/v1").rstrip("/")


def load_questions(path: Path) -> list[str]:
    questions: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.endswith("?"):
            questions.append(line)
    return questions


def evaluate_with_llm(question: str, context: str, answer: str, judge_model: str = "mistral-medium-latest") -> dict:
    """Utilise le LLM comme juge pour noter la réponse (RAGAS style enrichi).

    Évalue sur 5 critères avec raisonnement détaillé par critère,
    conçu pour permettre une comparaison robuste entre modèles LLM.
    """
    if not LLM_API_KEY:
        return {"error": "LLM_API_KEY non définie"}

    prompt = f"""Tu es un juge expert et impartial chargé d'évaluer une réponse générée par un système RAG (Retrieval-Augmented Generation).
Tu vas évaluer la réponse selon **cinq critères**, en donnant une note de 1 à 5 pour chaque.

## Critères d'évaluation

1. **Faithfulness (Fidélité)** — 1 à 5
   La réponse s'appuie-t-elle UNIQUEMENT sur le contexte fourni, sans halluciner d'informations externes ?
   - 5 : Chaque affirmation de la réponse est directement traçable dans le contexte.
   - 4 : Légères reformulations acceptables, mais aucune information inventée.
   - 3 : Quelques éléments sont inférés de manière raisonnable mais non explicites.
   - 2 : Plusieurs affirmations non fondées dans le contexte.
   - 1 : La majorité de la réponse est halluccinée.

2. **Answer Relevance (Pertinence de la réponse)** — 1 à 5
   La réponse adresse-t-elle directement et utilement la question posée ?
   - 5 : Réponse ciblée, exhaustive vis-à-vis de la question, sans hors-sujet.
   - 4 : Bonne pertinence, avec des éléments mineurs non directement demandés.
   - 3 : Partiellement pertinente ; certains aspects de la question ne sont pas traités.
   - 2 : La réponse touche au sujet mais ne répond pas vraiment à la question.
   - 1 : Réponse hors-sujet.

3. **Context Precision (Précision du Contexte)** — 1 à 5
   Le contexte retrouvé contenait-il effectivement les informations nécessaires pour répondre correctement ?
   - 5 : Le contexte contient toutes les informations nécessaires, bien ciblées.
   - 4 : Le contexte est pertinent mais manque de quelques détails.
   - 3 : Le contexte est partiellement utile ; plusieurs informations clés manquent.
   - 2 : Le contexte est vaguement lié au sujet.
   - 1 : Le contexte est non pertinent pour la question.

4. **Completeness (Exhaustivité de la réponse)** — 1 à 5
   La réponse couvre-t-elle TOUS les aspects de la question, en exploitant pleinement le contexte disponible ?
   - 5 : Tous les aspects de la question sont couverts, tous les détails utiles du contexte sont exploités.
   - 4 : Réponse quasi complète, un aspect mineur est omis.
   - 3 : Quelques points importants du contexte ne sont pas repris dans la réponse.
   - 2 : La réponse ne couvre que partiellement la question.
   - 1 : Réponse très lacunaire.

5. **Conciseness (Concision et clarté)** — 1 à 5
   La réponse est-elle claire, bien structurée et sans redondance inutile ?
   - 5 : Réponse bien structurée, va droit au but, aucune redondance.
   - 4 : Claire avec des redondances mineures.
   - 3 : Des passages pourraient être raccourcis ou mieux organisés.
   - 2 : Réponse confuse ou excessivement verbeuse.
   - 1 : Réponse désorganisée et difficilement compréhensible.

## Règles importantes

- **CONTACTS INJECTÉS** : Des informations de contact ou de loaboratoire (noms, e-mails, téléphones) sont souvent ajoutées à la fin de la réponse par notre système de manière automatique. Par conséquent, si un contact apparaît dans la réponse mais est ABSENT du [CONTEXTE RETROUVÉ], tu ne dois **JAMAIS le considérer comme une hallucination**. Ne pénalise en aucun cas la note de Faithfulness (Fidélité) pour des informations de contact ou des noms de services.
- **Score global** : Calcule un score global pondéré = (Faithfulness × 0.30) + (Answer Relevance × 0.25) + (Context Precision × 0.15) + (Completeness × 0.20) + (Conciseness × 0.10). Arrondis à 2 décimales.

## Données à évaluer

[QUESTION]
{question}

[CONTEXTE RETROUVÉ]
{context}

[RÉPONSE DU SYSTÈME]
{answer}

## Format de sortie

Formate ta réponse UNIQUEMENT en JSON valide avec la structure exacte suivante :
{{
    "faithfulness": <int 1-5>,
    "answer_relevance": <int 1-5>,
    "context_precision": <int 1-5>,
    "completeness": <int 1-5>,
    "conciseness": <int 1-5>,
    "overall_score": <float, score pondéré calculé>,
    "detailed_reasoning": {{
        "faithfulness": "<justification détaillée pour ce critère, avec exemples précis d'éléments vérifiés ou halluccinés>",
        "answer_relevance": "<justification détaillée pour ce critère>",
        "context_precision": "<justification détaillée : quelles informations étaient présentes ou absentes du contexte>",
        "completeness": "<justification détaillée : quels aspects de la question sont couverts ou manquants>",
        "conciseness": "<justification détaillée sur la structure et la clarté>"
    }},
    "hallucinated_elements": ["<liste des éléments de la réponse qui ne sont PAS dans le contexte, vide si aucun>"],
    "missing_from_answer": ["<liste des informations pertinentes du contexte qui n'ont PAS été exploitées dans la réponse, vide si aucune>"]
}}
"""
    headers = {"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": judge_model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(f"{LLM_BASE_URL}/chat/completions", headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        # Nettoyage au cas où le modèle encapsule le JSON dans des backticks
        content = content.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        return {"error": str(e)}



def resolve_query_files(base: Path, args: argparse.Namespace) -> list[Path]:
    if getattr(args, "query_files", None):
        return [Path(q) if Path(q).is_absolute() else (base / q) for q in args.query_files]

    if getattr(args, "query_file", None):
        query_file = Path(args.query_file)
        return [query_file if query_file.is_absolute() else (base / query_file)]

    return sorted(base.glob("Query*.txt"))


def build_output_path(base: Path, query_path: Path, default_name: str) -> Path:
    return base / f"{query_path.stem}_{default_name}"


def run_question(
    rag_path: Path,
    python_exec: str,
    question: str,
    log_file_arg: Path,
    timeout: int = 600,
    prompt_variant: str = "default",
    context_order: str = "preserve",
    k: int = 5,
    draft_model: str = "mistral-medium-latest",
    answer_model: str = "mistral-medium-latest",
    judge_model: str = "mistral-medium-latest",
) -> dict:
    
    def execute_rag(current_question: str) -> dict:
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp_json:
            tmp_json_path = Path(tmp_json.name)

        cmd = [
            python_exec,
            str(rag_path),
            "--question",
            current_question,
            "--log-file",
            str(log_file_arg),
            "--prompt-variant",
            prompt_variant,
            "--context-order",
            context_order,
            "--k",
            str(k),
            "--draft-model",
            draft_model,
            "--answer-model",
            answer_model,
            "--output-response-json",
            str(tmp_json_path),
        ]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=timeout)
            return {
                "returncode": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "tmp_json_path": tmp_json_path,
            }
        except Exception as exc:
            return {"returncode": -1, "stdout": "", "stderr": f"Exception: {exc}\n{traceback.format_exc()}", "tmp_json_path": None}

    # Premier essai avec la question pure (sans biaiser avec le labo LIFAT)
    t_rag_start = time.time()
    res = execute_rag(question)
    final_answer = extract_final_answer(res.get("stdout", ""))

    # Si le système demande dynamiquement l'acronyme du labo, on simule la réponse de l'utilisateur
    if "Merci d'indiquer l'acronyme de votre laboratoire" in final_answer:
        print("    -> [Requête de labo détectée] Simulation de la réponse utilisateur : LIFAT")
        
        # Nettoyage du fichier temporaire du premier essai
        if res.get("tmp_json_path") and res["tmp_json_path"].exists():
            try:
                res["tmp_json_path"].unlink()
            except OSError:
                pass
                
        # Relance avec l'information ajoutée
        res = execute_rag(f"{question} (Laboratoire: LIFAT)")
        final_answer = extract_final_answer(res.get("stdout", ""))
    rag_duration_s = round(time.time() - t_rag_start, 2)

    result_dict = {
        "returncode": res.get("returncode"),
        "stdout": res.get("stdout"),
        "stderr": res.get("stderr"),
        "rag_duration_s": rag_duration_s,
    }
    
    tmp_json_path = res.get("tmp_json_path")
    
    eval_duration_s = 0.0
    # Évaluation LLM-as-a-judge si le JSON a bien été généré
    if tmp_json_path and tmp_json_path.exists():
        try:
            with open(tmp_json_path, "r", encoding="utf-8") as f:
                rag_data = json.load(f)
            
            result_dict["exact_completion_tokens"] = rag_data.get("completion_tokens", 0)
            
            context_chunks = [hit.get("text", "") for hit in rag_data.get("retrieved_chunks", [])]
            context_str = "\n".join(context_chunks)
            
            t_eval_start = time.time()
            eval_scores = evaluate_with_llm(question, context_str, final_answer, judge_model=judge_model)
            eval_duration_s = round(time.time() - t_eval_start, 2)
            result_dict["evaluation"] = eval_scores
        except Exception as e:
            result_dict["evaluation"] = {"error": f"Parsing JSON / Evaluation failed: {e}"}
        finally:
            try:
                tmp_json_path.unlink()
            except OSError:
                pass

    result_dict["eval_duration_s"] = eval_duration_s
    result_dict["total_duration_s"] = round(rag_duration_s + eval_duration_s, 2)
    return result_dict


def extract_final_answer(stdout: str) -> str:
    match = re.search(r"Assistant\s*:\s*\n(?P<answer>.*?)(?:\n-{3,}\s*\n?|\Z)", stdout, flags=re.DOTALL)
    if match:
        return match.group("answer").strip()
    return stdout.strip()


def append_run_log(out_path: Path, question: str, result: dict) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().isoformat()
    with out_path.open("a", encoding="utf-8") as f:
        f.write("\n" + "#" * 120 + "\n")
        f.write(f"TIMESTAMP: {ts}\n")
        f.write("QUESTION:\n")
        f.write(question + "\n\n")
        f.write(f"RETURN CODE: {result.get('returncode')}\n\n")
        f.write(f"DRAFT MODEL: {result.get('draft_model', 'N/A')}\n")
        f.write(f"ANSWER MODEL: {result.get('answer_model', 'N/A')}\n")
        f.write(f"JUDGE MODEL: {result.get('judge_model', 'N/A')}\n")
        f.write(f"PROMPT VARIANT: {result.get('prompt_variant', 'default')}\n")
        f.write(f"CONTEXT ORDER: {result.get('context_order', 'preserve')}\n")
        f.write(f"REPEAT INDEX: {result.get('repeat_index', 1)}\n")
        f.write(f"RAG DURATION: {result.get('rag_duration_s', 'N/A')}s\n")
        f.write(f"EVAL DURATION: {result.get('eval_duration_s', 'N/A')}s\n")
        f.write(f"TOTAL DURATION: {result.get('total_duration_s', 'N/A')}s\n")
        f.write("STDOUT:\n")
        f.write(result.get("stdout", "") + "\n\n")
        
        evaluation = result.get("evaluation")
        if evaluation:
            f.write("LLM AS A JUDGE EVALUATION:\n")
            f.write(json.dumps(evaluation, indent=2, ensure_ascii=False) + "\n\n")

        f.write("STDERR:\n")
        f.write(result.get("stderr", "") + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query-file", type=str, default=None, help="Single file with questions to run")
    parser.add_argument(
        "--query-files",
        nargs="*",
        default=None,
        help="Several query files to run (default: all Query*.txt files in the Test folder)",
    )
    parser.add_argument("--rag-path", type=str, default="../RAGilaas/RAGilaas.py", help="Path to RAGilaas.py (relative to Test folder)")
    parser.add_argument("--output-log", type=str, default="rag_batch_run_logs.txt", help="Combined output log file (written in Test)")
    parser.add_argument("--output-json", type=str, default="rag_batch_trials.json", help="Structured JSON output for RS/PC analysis")
    parser.add_argument("--python", type=str, default=sys.executable, help="Python executable to run RAGilaas with")
    parser.add_argument("--timeout", type=int, default=600, help="Timeout per question in seconds")
    parser.add_argument("--repeat", type=int, default=1, help="Nombre de répétitions de l'ensemble des questions")
    parser.add_argument(
        "--prompt-variants",
        nargs="+",
        default=["default"],
        help="Variantes de prompt final à exécuter (ex: default pc_context_first pc_instructions_first).",
    )
    parser.add_argument(
        "--context-orders",
        nargs="+",
        default=["preserve"],
        help="Ordres de contexte à exécuter (ex: preserve reverse score_desc).",
    )
    parser.add_argument("--k", type=int, default=5, help="Nombre de chunks récupérés à demander à RAGilaas")
    parser.add_argument("--draft-model", type=str, default="mistral-medium-latest", help="Modèle LLM pour le routeur RAC et la génération HyDE")
    parser.add_argument("--answer-model", type=str, default="mistral-medium-latest", help="Modèle LLM pour la réponse finale")
    parser.add_argument("--judge-model", type=str, default="mistral-medium-latest", help="Modèle LLM pour l'évaluation (LLM-as-a-Judge)")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    rag_path = (base / args.rag_path) if not Path(args.rag_path).is_absolute() else Path(args.rag_path)

    query_paths = resolve_query_files(base, args)
    if not query_paths:
        print(f"No query files found in: {base}")
        raise SystemExit(2)

    if not rag_path.exists():
        print(f"RAGilaas.py not found: {rag_path}")
        raise SystemExit(3)

    total_questions = 0
    total_trials = 0

    for query_path in query_paths:
        if not query_path.exists():
            print(f"Query file not found: {query_path}")
            continue

        questions = load_questions(query_path)
        if not questions:
            print(f"No questions found in: {query_path.name}")
            continue

        output_log = (base / args.output_log) if len(query_paths) == 1 and not Path(args.output_log).is_absolute() else build_output_path(base, query_path, Path(args.output_log).name)
        output_json = (base / args.output_json) if len(query_paths) == 1 and not Path(args.output_json).is_absolute() else build_output_path(base, query_path, Path(args.output_json).name)
        output_json.parent.mkdir(parents=True, exist_ok=True)

        print(
            f"[{query_path.name}] Found {len(questions)} questions — running {args.repeat} repetition(s) "
            f"across {len(args.prompt_variants)} prompt variant(s) and {len(args.context_orders)} context order(s).\n"
            f"  Models: draft={args.draft_model}, answer={args.answer_model}, judge={args.judge_model}"
        )

        trial_records: list[dict[str, object]] = []
        trial_counter = 0

        for prompt_variant in args.prompt_variants:
            for context_order in args.context_orders:
                for repeat_index in range(1, max(1, args.repeat) + 1):
                    print(
                        f"[{query_path.name}] Configuration: prompt_variant={prompt_variant}, context_order={context_order}, repeat={repeat_index}"
                    )
                    for question_index, q in enumerate(questions, start=1):
                        trial_counter += 1
                        total_trials += 1
                        print(
                            f"[{query_path.name}] [{trial_counter}] Q{question_index}/{len(questions)} repeat {repeat_index} "
                            f"(truncated): {q[:80]!s}..."
                        )
                        result = run_question(
                            rag_path=rag_path,
                            python_exec=args.python,
                            question=q,
                            log_file_arg=output_log,
                            timeout=args.timeout,
                            prompt_variant=prompt_variant,
                            context_order=context_order,
                            k=args.k,
                            draft_model=args.draft_model,
                            answer_model=args.answer_model,
                            judge_model=args.judge_model,
                        )
                        result["prompt_variant"] = prompt_variant
                        result["context_order"] = context_order
                        result["repeat_index"] = repeat_index
                        result["question_index"] = question_index
                        result["question"] = q
                        result["query_file"] = query_path.name
                        result["draft_model"] = args.draft_model
                        result["answer_model"] = args.answer_model
                        result["judge_model"] = args.judge_model
                        result["final_answer"] = extract_final_answer(result.get("stdout", ""))
                        append_run_log(output_log, q, result)
                        trial_records.append(
                            {
                                "trial_id": trial_counter,
                                "query_file": query_path.name,
                                "question_index": question_index,
                                "question": q,
                                "repeat_index": repeat_index,
                                "prompt_variant": prompt_variant,
                                "context_order": context_order,
                                "draft_model": args.draft_model,
                                "answer_model": args.answer_model,
                                "judge_model": args.judge_model,
                                "rag_duration_s": result.get("rag_duration_s", 0),
                                "eval_duration_s": result.get("eval_duration_s", 0),
                                "total_duration_s": result.get("total_duration_s", 0),
                                "returncode": result.get("returncode"),
                                "final_answer": result.get("final_answer", ""),
                                "evaluation": result.get("evaluation", {}),
                                "exact_completion_tokens": result.get("exact_completion_tokens", 0),
                                "stdout": result.get("stdout", ""),
                                "stderr": result.get("stderr", ""),
                            }
                        )
                        eval_scores = result.get("evaluation", {})
                        timing_str = f"[RAG: {result.get('rag_duration_s', '?')}s | Eval: {result.get('eval_duration_s', '?')}s | Total: {result.get('total_duration_s', '?')}s]"
                        if "faithfulness" in eval_scores:
                            eval_str = (
                                f"| Faith: {eval_scores.get('faithfulness', '?')}/5 "
                                f"| Rel: {eval_scores.get('answer_relevance', '?')}/5 "
                                f"| Prec: {eval_scores.get('context_precision', '?')}/5 "
                                f"| Compl: {eval_scores.get('completeness', '?')}/5 "
                                f"| Conc: {eval_scores.get('conciseness', '?')}/5 "
                                f"| Overall: {eval_scores.get('overall_score', '?')}"
                            )
                        else:
                            eval_str = ""
                        print(f"[{query_path.name}] -> return code {result.get('returncode')} {timing_str} {eval_str}. Logged.")

        payload = {
            "generated_at": datetime.datetime.now().isoformat(),
            "query_file": query_path.name,
            "question_count": len(questions),
            "repeat": max(1, args.repeat),
            "prompt_variants": args.prompt_variants,
            "context_orders": args.context_orders,
            "draft_model": args.draft_model,
            "answer_model": args.answer_model,
            "judge_model": args.judge_model,
            "trials": trial_records,
        }
        output_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

        total_questions += len(questions)
        print(f"[{query_path.name}] Done. Log: {output_log}")
        print(f"[{query_path.name}] Structured trials JSON: {output_json}")

    print(f"All done. Total query files: {len(query_paths)} | Total questions: {total_questions} | Total trials: {total_trials}")


if __name__ == "__main__":
    main()
