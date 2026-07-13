from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import argparse
import json
from loguru import logger
import re
import shlex
import shutil
import subprocess
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import fitz


@dataclass
class PrecheckResult:
    """
    Résultat de l'analyse préliminaire d'un fichier PDF avant conversion.
    Contient des métadonnées comme le nombre de pages, si le PDF est chiffré, et la qualité du texte.
    """
    exists: bool
    file_size_mb: float
    page_count: int
    is_encrypted: bool
    readable_with_fitz: bool
    sample_text_chars: int
    sample_alpha_ratio: float
    cid_detected_in_sample: bool
    warnings: list[str]


@dataclass
class MarkerAttempt:
    """
    Représente une tentative d'exécution de Marker sur un PDF avec des arguments spécifiques (ex: force-ocr).
    """
    name: str
    command: list[str]
    return_code: int | None
    duration_s: float
    status: str
    stdout_tail: str
    stderr_tail: str


@dataclass
class OutputQuality:
    """
    Évaluation de la qualité du fichier Markdown généré par Marker (ratio caractères alphanumériques, mots, etc.).
    """
    md_files_found: int
    total_chars: int
    total_words: int
    alpha_ratio: float
    cid_ratio: float
    placeholder_count: int
    quality_ok: bool
    reason: str


@dataclass
class MarkerRunResult:
    """
    Bilan global de l'exécution de Marker pour un fichier PDF donné, incluant le precheck, les tentatives et la qualité.
    """
    pdf_name: str
    pdf_path: str
    precheck: PrecheckResult
    attempts: list[MarkerAttempt]
    quality: OutputQuality
    status: str
    used_attempt: str


def find_project_root(current_file: Path) -> Path:
    for parent in [current_file.parent, *current_file.parents]:
        if (parent / "requirements.txt").exists():
            return parent
    return current_file.parents[2]


def tail_text(text: str, max_chars: int = 1200) -> str:
    if len(text) <= max_chars:
        return text
    return text[-max_chars:]





def _safe_div(num: float, den: float) -> float:
    return num / den if den else 0.0


def marker_pdf_dir(pdf_path: Path, output_dir: Path) -> Path:
    return output_dir / pdf_path.stem


def marker_md_path(pdf_path: Path, output_dir: Path) -> Path:
    return marker_pdf_dir(pdf_path, output_dir) / f"{pdf_path.stem}.md"


def marker_output_exists(pdf_path: Path, output_dir: Path) -> bool:
    return marker_md_path(pdf_path, output_dir).exists()


def _marker_help_text(marker_cmd: str) -> str:
    try:
        help_proc = subprocess.run([marker_cmd, "--help"], capture_output=True, text=True)
        return (help_proc.stdout or "") + "\n" + (help_proc.stderr or "")
    except Exception:
        return ""


def _resolve_marker_command() -> str:
    import sys
    import os
    
    bin_dir = Path(sys.executable).parent
    for candidate in ("marker_single", "marker"):
        # Check first in the same directory as python (venv/bin)
        candidate_path = bin_dir / candidate
        if candidate_path.is_file() and os.access(candidate_path, os.X_OK):
            return str(candidate_path)
            
        # Fallback to PATH
        marker_cmd = shutil.which(candidate)
        if marker_cmd is not None:
            return marker_cmd
            
    raise RuntimeError(
        "Commande 'marker_single' ou 'marker' introuvable. Installe Marker puis relance (ex: pip install marker-pdf)."
    )


def _resolve_force_ocr_args(help_text: str) -> list[str]:
    # Désactivé pour que ça reste rapide (l'utilisateur préfère la version rapide de PyMuPDF)
    return []


def _resolve_lang_args(help_text: str) -> list[str]:
    if re.search(r"--languages\b", help_text):
        return ["--languages", "French"]
    if re.search(r"--langs\b", help_text):
        return ["--langs", "French"]
    if re.search(r"--language\b", help_text):
        return ["--language", "French"]
    if re.search(r"--lang\b", help_text):
        return ["--lang", "French"]
    return []


def precheck_pdf(pdf_path: Path) -> PrecheckResult:
    warnings: list[str] = []
    exists = pdf_path.exists()
    if not exists:
        return PrecheckResult(
            exists=False,
            file_size_mb=0.0,
            page_count=0,
            is_encrypted=False,
            readable_with_fitz=False,
            sample_text_chars=0,
            sample_alpha_ratio=0.0,
            cid_detected_in_sample=False,
            warnings=["Fichier introuvable"],
        )

    file_size_mb = round(pdf_path.stat().st_size / (1024 * 1024), 3)
    if file_size_mb <= 0:
        warnings.append("Fichier vide")

    page_count = 0
    is_encrypted = False
    readable_with_fitz = False
    sample_text = ""

    try:
        with fitz.open(pdf_path) as doc:
            page_count = len(doc)
            is_encrypted = bool(doc.is_encrypted)
            readable_with_fitz = True

            # Pré-check rapide: texte des 2 premières pages max.
            for i in range(min(2, page_count)):
                try:
                    sample_text += doc[i].get_text("text") + "\n"
                except Exception:
                    warnings.append(f"Lecture texte impossible page {i+1}")

    except Exception as exc:
        warnings.append(f"Ouverture PyMuPDF échouée: {exc}")

    sample_text_chars = len(sample_text)
    sample_alpha_ratio = _safe_div(sum(c.isalpha() for c in sample_text), max(1, len(sample_text)))
    cid_detected = bool(re.search(r"\(cid:\d+\)", sample_text))

    if page_count == 0:
        warnings.append("Aucune page détectée")
    if is_encrypted:
        warnings.append("PDF chiffré/protégé")
    if sample_text_chars < 40:
        warnings.append("Peu ou pas de couche texte détectée (probable scan)")
    if cid_detected:
        warnings.append("Pattern CID détecté dans la couche texte")

    return PrecheckResult(
        exists=exists,
        file_size_mb=file_size_mb,
        page_count=page_count,
        is_encrypted=is_encrypted,
        readable_with_fitz=readable_with_fitz,
        sample_text_chars=sample_text_chars,
        sample_alpha_ratio=round(sample_alpha_ratio, 4),
        cid_detected_in_sample=cid_detected,
        warnings=warnings,
    )


def evaluate_marker_output(pdf_path: Path, output_dir: Path) -> OutputQuality:
    exact_md = marker_md_path(pdf_path, output_dir)
    if exact_md.exists():
        md_files = [exact_md]
    else:
        stem = pdf_path.stem.lower()
        md_files = [p for p in output_dir.rglob("*.md") if stem in p.stem.lower() or stem in str(p).lower()]

    full_text = ""
    for md in md_files:
        try:
            full_text += md.read_text(encoding="utf-8", errors="ignore") + "\n"
        except Exception:
            continue

    chars = len(full_text)
    words = len(full_text.split())
    alpha_ratio = _safe_div(sum(c.isalpha() for c in full_text), max(1, chars))
    cid_matches = re.findall(r"\(cid:\d+\)", full_text)
    cid_ratio = _safe_div(len(cid_matches), max(1, words))
    placeholder_count = full_text.count("<!-- image -->")

    quality_ok = True
    reason = "ok"
    if chars < 150 or words < 30:
        quality_ok = False
        reason = "sortie trop courte"
    elif alpha_ratio < 0.35:
        quality_ok = False
        reason = "alpha_ratio faible"
    elif cid_ratio > 0.15:
        quality_ok = False
        reason = "CID détecté"

    return OutputQuality(
        md_files_found=len(md_files),
        total_chars=chars,
        total_words=words,
        alpha_ratio=round(alpha_ratio, 4),
        cid_ratio=round(cid_ratio, 4),
        placeholder_count=placeholder_count,
        quality_ok=quality_ok,
        reason=reason,
    )


def run_marker_attempt(
    marker_cmd: str,
    pdf_path: Path,
    output_dir: Path,
    max_pages: int | None,
    extra_args: list[str],
    name: str,
    logger: logger,
    live_progress: bool,
) -> MarkerAttempt:
    help_text = _marker_help_text(marker_cmd)
    
    cmd = [marker_cmd, str(pdf_path)]
    
    # Force CPU to avoid Mac MPS deadlock with Transformers
    import os
    env = os.environ.copy()
    if "--output_dir" in help_text:
        cmd.extend(["--output_dir", str(output_dir)])
    else:
        cmd.append(str(output_dir))

    if max_pages is not None and max_pages > 0:
        if "--max_pages" in help_text:
            cmd.extend(["--max_pages", str(max_pages)])
        else:
            page_end = max_pages - 1
            cmd.extend(["--page_range", f"0-{page_end}"])

    if extra_args:
        cmd.extend(extra_args)

    start = time.perf_counter()
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=env,
    )

    combined_output = ""
    if proc.stdout is not None:
        for raw_line in proc.stdout:
            line = raw_line.rstrip("\n")
            if live_progress and line.strip():
                logger.info(f"[MARKER] {line}")
            combined_output += raw_line
            if len(combined_output) > 120_000:
                combined_output = combined_output[-120_000:]

    return_code = proc.wait()
    duration = time.perf_counter() - start

    return MarkerAttempt(
        name=name,
        command=cmd,
        return_code=return_code,
        duration_s=round(duration, 3),
        status="ok" if return_code == 0 else "error",
        stdout_tail=tail_text(combined_output),
        stderr_tail="",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Test Marker sur un dossier de PDF")
    parser.add_argument(
        "--input-dir",
        type=str,
        default="data/downloads/Chatbot DRV",
        help="Dossier PDF à tester",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="TestExtraction/data/marker_markdown/PDF2",
        help="Dossier de sortie Marker",
    )
    parser.add_argument(
        "--report",
        type=str,
        default="TestExtraction/logs/marker_test_report.json",
        help="Rapport JSON des exécutions",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Limiter le nombre de PDF testés (0 = tous)",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="Limiter le nombre de pages par PDF pour un test rapide (0 = sans limite)",
    )
    parser.add_argument(
        "--retry-extra-args",
        type=str,
        default="",
        help="Arguments supplémentaires Marker pour une 2e tentative (ex: '--use_llm --force_ocr')",
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default="TestExtraction/logs/marker_test_run.log",
        help="Fichier log détaillé",
    )
    parser.add_argument(
        "--live-progress",
        action="store_true",
        help="Affiche les logs de progression Marker en direct dans le terminal",
    )
    args = parser.parse_args()

    current_file = Path(__file__).resolve()
    project_root = find_project_root(current_file)

    input_dir = (project_root / args.input_dir).resolve() if not Path(args.input_dir).is_absolute() else Path(args.input_dir)
    output_dir = (project_root / args.output_dir).resolve() if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    report_path = (project_root / args.report).resolve() if not Path(args.report).is_absolute() else Path(args.report)
    log_path = (project_root / args.log_file).resolve() if not Path(args.log_file).is_absolute() else Path(args.log_file)
    from Utilitaire.Utbox import setup_global_logger
    logger = setup_global_logger(log_prefix="Update")

    if not input_dir.exists():
        raise FileNotFoundError(f"Dossier introuvable: {input_dir}")

    marker_cmd = _resolve_marker_command()
    help_text = _marker_help_text(marker_cmd)
    marker_args = _resolve_lang_args(help_text) + _resolve_force_ocr_args(help_text)

    output_dir.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(input_dir.rglob("*.pdf"))
    if args.max_files > 0:
        pdf_files = pdf_files[: args.max_files]

    if not pdf_files:
        raise RuntimeError(f"Aucun PDF trouvé dans: {input_dir}")

    max_pages = args.max_pages if args.max_pages > 0 else None
    retry_extra_args = shlex.split(args.retry_extra_args) if args.retry_extra_args.strip() else []

    results: list[MarkerRunResult] = []
    ok_count = 0
    skipped_count = 0
    quality_fail_count = 0

    logger.info(f"Marker command: {marker_cmd}")
    logger.info(f"PDF trouvés: {len(pdf_files)}")
    logger.info(f"Log détaillé: {log_path}")
    logger.info(f"Dossier de sortie: {output_dir}")
    if marker_args:
        logger.info(f"Options Marker auto-détectées: {marker_args}")
    if retry_extra_args:
        logger.info(f"2e tentative Marker activée avec args: {retry_extra_args}")

    for idx, pdf_path in enumerate(pdf_files, start=1):
        rel_path = pdf_path.relative_to(input_dir)
        target_out_dir = output_dir / rel_path.parent
        target_out_dir.mkdir(parents=True, exist_ok=True)

        if marker_output_exists(pdf_path, target_out_dir):
            logger.info(
                f"[{idx}/{len(pdf_files)}] Déjà traité, on saute -> {pdf_path.name} "
                f"(sortie existante: {marker_md_path(pdf_path, target_out_dir)})"
            )
            precheck = precheck_pdf(pdf_path)
            quality = evaluate_marker_output(pdf_path, target_out_dir)
            result = MarkerRunResult(
                pdf_name=pdf_path.name,
                pdf_path=str(pdf_path),
                precheck=precheck,
                attempts=[],
                quality=quality,
                status="skipped",
                used_attempt="already_present",
            )
            results.append(result)
            skipped_count += 1
            continue

        logger.info(f"[{idx}/{len(pdf_files)}] Pré-check -> {pdf_path.name}")
        precheck = precheck_pdf(pdf_path)

        for w in precheck.warnings:
            logger.warning(f"{pdf_path.name} | precheck: {w}")

        attempts: list[MarkerAttempt] = []

        logger.info(f"[{idx}/{len(pdf_files)}] Marker (attempt_1_default) -> {pdf_path.name}")
        first = run_marker_attempt(
            marker_cmd=marker_cmd,
            pdf_path=pdf_path,
            output_dir=target_out_dir,
            max_pages=max_pages,
            extra_args=marker_args,
            name="attempt_1_default",
            logger=logger,
            live_progress=args.live_progress,
        )
        attempts.append(first)

        quality = evaluate_marker_output(pdf_path, target_out_dir)

        if first.status != "ok" or not quality.quality_ok:
            if retry_extra_args:
                logger.info(f"[{idx}/{len(pdf_files)}] Marker (attempt_2_retry) -> {pdf_path.name}")
                second = run_marker_attempt(
                    marker_cmd=marker_cmd,
                    pdf_path=pdf_path,
                    output_dir=target_out_dir,
                    max_pages=max_pages,
                    extra_args=marker_args + retry_extra_args,
                    name="attempt_2_retry",
                    logger=logger,
                    live_progress=args.live_progress,
                )
                attempts.append(second)
                quality = evaluate_marker_output(pdf_path, target_out_dir)

        final_attempt = attempts[-1]
        final_status = "ok" if final_attempt.status == "ok" and quality.quality_ok else "error"

        if not quality.quality_ok:
            quality_fail_count += 1
            logger.warning(f"{pdf_path.name} | qualité insuffisante: {quality.reason}")

        result = MarkerRunResult(
            pdf_name=pdf_path.name,
            pdf_path=str(pdf_path),
            precheck=precheck,
            attempts=attempts,
            quality=quality,
            status=final_status,
            used_attempt=final_attempt.name,
        )
        results.append(result)

        if result.status == "ok":
            ok_count += 1
        elif result.status == "skipped":
            skipped_count += 1

        logger.info(
            f"{pdf_path.name} | status={result.status} | attempt={result.used_attempt} | "
            f"quality_ok={quality.quality_ok} | words={quality.total_words} | alpha={quality.alpha_ratio}"
        )

    payload: dict[str, Any] = {
        "input_dir": str(input_dir),
        "output_dir": str(output_dir),
        "marker_cmd": marker_cmd,
        "retry_extra_args": retry_extra_args,
        "log_file": str(log_path),
        "total": len(results),
        "success": ok_count,
        "skipped": skipped_count,
        "failed": len(results) - ok_count - skipped_count,
        "quality_failures": quality_fail_count,
        "results": [asdict(r) for r in results],
    }

    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    logger.info("=== Résumé Marker ===")
    logger.info(
        f"Succès: {ok_count} | Ignorés: {skipped_count} | Échecs: {len(results) - ok_count - skipped_count} | "
        f"Échecs qualité: {quality_fail_count}"
    )
    logger.info(f"Rapport: {report_path}")


if __name__ == "__main__":
    main()
