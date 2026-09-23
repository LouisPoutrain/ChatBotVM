from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def resolve_python_executable(repo_root: Path) -> str:
	venv_python = repo_root / ".venv" / "bin" / "python"
	return str(venv_python if venv_python.exists() else Path(sys.executable))


def run_command(command: list[str], cwd: Path) -> None:
	print("\n>>", " ".join(command))
	completed = subprocess.run(command, cwd=cwd)
	if completed.returncode != 0:
		raise SystemExit(completed.returncode)


def main() -> None:
	parser = argparse.ArgumentParser(description="Run a full RS/PC benchmark on a query file.")
	parser.add_argument("--query-file", default="Query.txt", help="Query file located in the Test folder.")
	parser.add_argument("--repeat", type=int, default=10, help="Number of repetitions per configuration.")
	parser.add_argument("--output-dir", default="Results/rs_pc", help="Directory where benchmark outputs are written.")
	parser.add_argument(
		"--prompt-variants",
		nargs="+",
		default=["default", "pc_context_first", "pc_instructions_first"],
		help="Prompt variants to evaluate for PC.",
	)
	parser.add_argument(
		"--context-orders",
		nargs="+",
		default=["preserve", "reverse", "score_desc"],
		help="Context ordering strategies to evaluate for PC.",
	)
	parser.add_argument("--k", type=int, default=5, help="Number of chunks requested from RAGilaas.")
	args = parser.parse_args()

	base_dir = Path(__file__).resolve().parent
	repo_root = base_dir.parent
	query_file = Path(args.query_file)
	if not query_file.is_absolute():
		if (base_dir / "Queries" / args.query_file).exists():
			query_file = base_dir / "Queries" / args.query_file
		else:
			query_file = base_dir / query_file

	if not query_file.exists():
		raise FileNotFoundError(f"Query file not found: {query_file}")

	output_dir = Path(args.output_dir)
	if not output_dir.is_absolute():
		output_dir = base_dir / output_dir
	output_dir.mkdir(parents=True, exist_ok=True)

	runner_script = base_dir / "run_queries_ragilaas.py"
	metrics_script = base_dir / "RS&PC.py"
	python_exec = resolve_python_executable(repo_root)

	trials_json = output_dir / f"{query_file.stem}_rag_batch_trials.json"
	run_logs = output_dir / f"{query_file.stem}_rag_batch_run_logs.txt"
	summary_json = output_dir / f"{query_file.stem}_rs_pc_summary.json"

	run_command(
		[
			python_exec,
			str(runner_script),
			"--query-file",
			str(query_file),
			"--repeat",
			str(args.repeat),
			"--output-log",
			str(run_logs),
			"--output-json",
			str(trials_json),
			"--python",
			python_exec,
			"--prompt-variants",
			*args.prompt_variants,
			"--context-orders",
			*args.context_orders,
			"--k",
			str(args.k),
		],
		cwd=base_dir,
	)

	run_command(
		[
			python_exec,
			str(metrics_script),
			"--input",
			str(trials_json),
			"--output",
			str(summary_json),
		],
		cwd=base_dir,
	)

	print("\nBenchmark complete.")
	print(f"Trials JSON: {trials_json}")
	print(f"Run logs: {run_logs}")
	print(f"Summary JSON: {summary_json}")


if __name__ == "__main__":
	main()