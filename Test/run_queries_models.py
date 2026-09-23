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

import requests


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
        # Keep only likely questions from Query.txt
        if line.endswith("?") or line.endswith("？"):
            questions.append(line)
    return questions


def discover_models(base_url: str, headers: dict[str, str], exclude: set[str]) -> list[str]:
    url = base_url.rstrip("/") + "/models"
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    models = []
    # Accept either OpenAI-like list or plain list
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
        query_file = cur / "Test" / "Query.txt"
        rag_script = cur / "RAGilaas" / "RAGilaas.py"
        if not rag_script.exists():
            rag_script = cur / "RAG" / "RAGilaas" / "RAGilaas.py"
        if query_file.exists() and rag_script.exists():
            return cur, query_file, rag_script
        cur = cur.parent
    raise FileNotFoundError("Impossible de trouver la racine projet avec Test/Query.txt et RAGilaas/RAGilaas.py")


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
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "cmd": cmd,
    }


def extract_final_answer(stdout: str) -> str:
    match = re.search(r"Assistant\s*:\s*\n(?P<answer>.*?)(?:\n-{3,}\s*\n?|\Z)", stdout, flags=re.DOTALL)
    if match:
        return match.group("answer").strip()
    return stdout.strip()


def main():
    parser = argparse.ArgumentParser(description="Lance RAGilaas sur toutes les questions de Query.txt pour plusieurs modèles")
    parser.add_argument("--query-file", type=str, default=None, help="Fichier des questions (par défaut: Test/Query.txt)")
    parser.add_argument("--k", type=int, default=6, help="Nombre de chunks pour RAGilaas")
    parser.add_argument("--timeout", type=int, default=600, help="Timeout par question (secondes)")
    parser.add_argument("--python", type=str, default=sys.executable, help="Interpréteur Python à utiliser")
    parser.add_argument("--sleep-between", type=float, default=0.5, help="Pause entre 2 questions")
    parser.add_argument("--max-models", type=int, default=0, help="Limiter le nombre de modèles (0 = tous)")
    parser.add_argument("--max-questions", type=int, default=0, help="Limiter le nombre de questions (0 = toutes)")
    parser.add_argument("--dry-run", action="store_true", help="N'exécute pas RAGilaas, prépare seulement le plan")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    try:
        root, default_query_file, rag_script = find_project_root(script_dir)
    except FileNotFoundError as exc:
        print(str(exc))
        return

    if args.query_file:
        query_file = Path(args.query_file)
        if not query_file.is_absolute():
            query_file = root / query_file
    else:
        query_file = default_query_file

    if not query_file.exists():
        print(f"Query file not found: {query_file}")
        return

    test_dir = root / "Test"

    env = load_env(root)
    api_key = env.get("LLM_API_KEY") or os.getenv("LLM_API_KEY")
    base_url = (env.get("LLM_BASE_URL") or os.getenv("LLM_BASE_URL") or "https://llm.ilaas.fr/v1").rstrip("/")
    if not api_key:
        print("LLM_API_KEY missing in .env and environment variables")
        return

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Models to exclude (user request)
    excluded = {"llama-3.3-70b", "gpt-oss-120b", "llama-3.1-8b"}

    print("Discovering models from API...")
    try:
        models = discover_models(base_url, headers, excluded)
    except Exception as e:
        print(f"Failed to discover models: {e}")
        return

    if not models:
        print("No models discovered.")
        return

    if args.max_models > 0:
        models = models[: args.max_models]

    print(f"Models selected (after exclusion): {models}")

    questions = load_questions(query_file)
    if args.max_questions > 0:
        questions = questions[: args.max_questions]

    if not questions:
        print(f"No questions found in {query_file}")
        return

    print(f"Loaded {len(questions)} questions from {query_file}")

    out_dir = test_dir / "results_ragilaas_models"
    out_dir.mkdir(parents=True, exist_ok=True)

    run_tag = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    summary: dict[str, Any] = {
        "generated_at": datetime.datetime.now().isoformat(),
        "query_file": str(query_file),
        "excluded_models": sorted(excluded),
        "models": models,
        "question_count": len(questions),
        "runs": {},
        "rag_script": str(rag_script),
        "base_url": base_url,
        "dry_run": bool(args.dry_run),
    }

    for model in models:
        print(f"Running RAGilaas for model: {model}")
        model_results = []
        model_log_file = out_dir / f"ragilaas_{model.replace('/', '_').replace(':', '_')}_{run_tag}.log"

        for idx, q in enumerate(questions, start=1):
            print(f"  - Q{idx}/{len(questions)}")
            if args.dry_run:
                entry = {
                    "question_index": idx,
                    "question": q,
                    "returncode": None,
                    "stdout": "",
                    "stderr": "",
                    "final_answer": "",
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
                    entry = {
                        "question_index": idx,
                        "question": q,
                        "returncode": res.get("returncode"),
                        "stdout": res.get("stdout", ""),
                        "stderr": res.get("stderr", ""),
                        "final_answer": extract_final_answer(res.get("stdout", "")),
                        "cmd": res.get("cmd", []),
                    }
                except Exception as e:
                    entry = {
                        "question_index": idx,
                        "question": q,
                        "error": str(e),
                    }
            model_results.append(entry)
            time.sleep(args.sleep_between)

        out_file = out_dir / f"{model.replace('/', '_').replace(':', '_')}.json"
        out_file.write_text(json.dumps(model_results, ensure_ascii=False, indent=2), encoding="utf-8")
        summary["runs"][model] = {
            "questions": len(model_results),
            "results_file": str(out_file),
            "rag_log_file": str(model_log_file),
        }

    summary_file = out_dir / "summary.json"
    summary_file.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done. Results saved in {out_dir}")


if __name__ == "__main__":
    main()
