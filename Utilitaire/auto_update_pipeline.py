import argparse
import subprocess
import sys
import shutil
from pathlib import Path

# Ajouter les chemins nécessaires
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "Utilitaire"))

from Utbox import UTBoxDownloader

def main() -> None:
    """
    Point d'entrée du pipeline de mise à jour automatisée.
    
    Étapes :
    1. Synchronisation des fichiers depuis UTBOX via WebDAV (téléchargement différentiel).
    2. Mise à jour éventuelle des documents et bases Qdrant du routeur expert (RAC).
    3. Conversion des nouveaux PDF en Markdown via Marker.
    4. Indexation vectorielle des nouveaux Markdown dans Qdrant (BV).
    """
    from Utbox import setup_global_logger
    logger = setup_global_logger(log_prefix="Update")

    parser = argparse.ArgumentParser(description="Pipeline automatisé de mise à jour du ChatBot depuis UTBOX")
    parser.add_argument(
        "--share-url", 
        default="https://utbox.univ-tours.fr/s/mmWZHxXHHZSgybT/download",
        help="Lien de partage public UTBOX"
    )
    args = parser.parse_args()

    logger.info("============================================================")
    logger.info(" ÉTAPE 1: Synchronisation WebDAV UTBOX")
    logger.info("============================================================")
    downloader = UTBoxDownloader(timeout=120)
    downloads_dir = PROJECT_ROOT / "data" / "downloads"
    
    # 1. Synchronisation incrémentale
    try:
        new_files = downloader.sync_via_zip(
            share_url=args.share_url,
            output_dir=str(downloads_dir)
        )
    except Exception as e:
        logger.error(f"[ERREUR FATALE] Impossible de synchroniser UTBOX: {e}")
        sys.exit(1)

    if not new_files:
        logger.info("[INFO] Aucun nouveau fichier détecté. La base de données est déjà à jour.")
        logger.info("Fin du pipeline.")
        return

    logger.info(f"[INFO] {len(new_files)} fichier(s) nouveau(x) ou modifié(s) téléchargé(s).")

    logger.info("============================================================")
    logger.info(" ÉTAPE 1.5: Synchronisation des données RAC")
    logger.info("============================================================")
    rac_local_dir = PROJECT_ROOT / "RAC"
    count_rac_synced = 0
    
    # On scanne le dossier de téléchargement pour trouver les fichiers RAC
    # afin de les copier s'ils sont nouveaux, ou s'ils manquent en local
    for path in downloads_dir.rglob("*"):
        if not path.is_file(): continue
        
        try:
            rel_parts = path.relative_to(downloads_dir).parts
        except ValueError:
            continue
            
        if "RAC" in rel_parts:
            rac_index = rel_parts.index("RAC")
            rel_path_after_rac = Path(*rel_parts[rac_index+1:])
            
            if rel_path_after_rac.parts and (rel_path_after_rac.parts[0] == "Data" or str(rel_path_after_rac) == "ContactRole.txt"):
                target_path = rac_local_dir / rel_path_after_rac
                
                # On copie si le fichier a été nouvellement téléchargé (présent dans new_files)
                # OU s'il n'existe plus en local (supprimé par l'utilisateur)
                if path in new_files or not target_path.exists():
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(path, target_path)
                    logger.info(f"  -> RAC mis à jour / restauré : {target_path.name}")
                    count_rac_synced += 1
                
    if count_rac_synced > 0:
        logger.info(f"[INFO] {count_rac_synced} fichier(s) RAC synchronisé(s).")
        logger.info("============================================================")
        logger.info(" ÉTAPE 1.6: Indexation Qdrant (RAC)")
        logger.info("============================================================")
        rac_qdrant_script = PROJECT_ROOT / "RAC" / "qdrant.py"
        try:
            subprocess.run([sys.executable, str(rac_qdrant_script)], check=True)
            logger.info("[INFO] Base Qdrant RAC mise à jour avec succès.")
        except subprocess.CalledProcessError as e:
            logger.error(f"[ERREUR FATALE] Échec de la mise à jour Qdrant RAC: {e}")
            sys.exit(1)
    else:
        logger.info("[INFO] Aucun fichier RAC à synchroniser.")

    logger.info("============================================================")
    logger.info(" ÉTAPE 2: Conversion PDF vers Markdown (Marker)")
    logger.info("============================================================")
    marker_script = PROJECT_ROOT / "Utilitaire" / "Marker.py"
    marker_output_dir = PROJECT_ROOT / "PDF2"
    
    # On passe input-dir pour être sûr de repointer sur le bon dossier racine
    # et output-dir pour expliciter où écrire les markdown
    try:
        subprocess.run([
            sys.executable, str(marker_script),
            "--input-dir", str(downloads_dir / "Chatbot DRV" / "ChatBot"),
            "--output-dir", str(marker_output_dir)
        ], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"[ERREUR FATALE] Échec de la conversion Marker: {e}")
        sys.exit(1)

    logger.info("============================================================")
    logger.info(" ÉTAPE 3: Indexation dans la base vectorielle (Qdrant)")
    logger.info("============================================================")
    bv_script = PROJECT_ROOT / "BV" / "BV.py"
    
    # On passe explicitement --markdown-dir pour qu'il indexe les bons fichiers
    try:
        subprocess.run([
            sys.executable, str(bv_script),
            "--markdown-dir", str(marker_output_dir)
        ], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"[ERREUR FATALE] Échec de l'indexation Qdrant: {e}")
        sys.exit(1)

    logger.info("============================================================")
    logger.info(" MISE À JOUR TERMINÉE AVEC SUCCÈS")
    logger.info("============================================================")

if __name__ == "__main__":
    main()
