#!/usr/bin/env python3
"""
Script d'indexation complète de toutes les bases vectorielles Qdrant :
1. Base des contacts administratifs (RAC -> collection infocontact)
2. Base documentaire Markdown (BV -> collection pdf2_documents)
"""
from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    print("=" * 60)
    print("1/2 - Indexation de la base des contacts administratifs (RAC)")
    print("=" * 60)
    rac_script = PROJECT_ROOT / "RAC" / "qdrant.py"
    subprocess.run([sys.executable, str(rac_script)], check=True)

    print("\n" + "=" * 60)
    print("2/2 - Indexation du corpus documentaire Markdown (BV)")
    print("=" * 60)
    bv_script = PROJECT_ROOT / "BV" / "BV.py"
    pdf2_dir = PROJECT_ROOT / "PDF2"
    subprocess.run([sys.executable, str(bv_script), "--markdown-dir", str(pdf2_dir)], check=True)

    print("\n" + "=" * 60)
    print(" Indexation complète terminée avec succès dans Qdrant !")
    print("=" * 60)

if __name__ == "__main__":
    main()
