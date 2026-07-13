from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


# Mot de type Prénom/Nom avec accents, tirets, apostrophes
NAME_TOKEN = r"[A-ZÀ-ÖØ-Ý][a-zà-öø-ÿ]+(?:[-'][A-ZÀ-ÖØ-Ý]?[a-zà-öø-ÿ]+)*"
# NOM en majuscules (ex: DUPONT, LE-BRUN)
UPPER_NAME_TOKEN = r"[A-ZÀ-ÖØ-Ý]{2,}(?:-[A-ZÀ-ÖØ-Ý]{2,})*"

NAME_PATTERNS = [
	re.compile(rf"\b({NAME_TOKEN})\s+({NAME_TOKEN})\b"),
	re.compile(rf"\b({UPPER_NAME_TOKEN})\s+({NAME_TOKEN})\b"),
	re.compile(rf"\b({NAME_TOKEN})\s+({UPPER_NAME_TOKEN})\b"),
]

# Filtres simples pour éviter des faux positifs fréquents
EXCLUDED_WORDS = {
	"Université",
	"Doctorat",
	"Thèse",
	"Recherche",
	"Inscription",
	"Master",
	"Licence",
	"Année",
	"Service",
	"Direction",
	"Présidence",
	"Document",
	"Dossier",
	"Pièce",
	"Liste",
	"Procédure",
	"Vademecum",
	"Janvier",
	"Février",
	"Mars",
	"Avril",
	"Mai",
	"Juin",
	"Juillet",
	"Août",
	"Septembre",
	"Octobre",
	"Novembre",
	"Décembre",
}


def _is_mostly_upper(token: str) -> bool:
	"""
	Vérifie si un token est majoritairement composé de lettres majuscules.
	Utile pour différencier les noms de famille (souvent en majuscules) des prénoms.
	"""
	letters = [c for c in token if c.isalpha()]
	return bool(letters) and all(c.isupper() for c in letters)


def _is_valid_name_part(token: str) -> bool:
	"""
	Vérifie si une chaîne peut être considérée comme une partie valide d'un nom/prénom.
	Exclut les mots-clés fréquents et les acronymes courts.
	"""
	if token in EXCLUDED_WORDS:
		return False
	# Evite les segments entièrement en majuscules courts (ex: DR, UE)
	if _is_mostly_upper(token) and len(token) <= 3:
		return False
	return True


def extract_person_names_from_text(text: str) -> list[str]:
	"""
	Extrait les noms et prénoms d'une chaîne de texte en utilisant des expressions régulières.
	Normalise le format pour retourner "Prénom Nom".
	
	Args:
		text (str): Le texte source à analyser.
		
	Returns:
		list[str]: Une liste de noms/prénoms identifiés et normalisés.
	"""
	names: list[str] = []

	for pattern in NAME_PATTERNS:
		for match in pattern.finditer(text):
			part1, part2 = match.group(1), match.group(2)

			if not (_is_valid_name_part(part1) and _is_valid_name_part(part2)):
				continue

			# Normalisation légère de sortie
			if _is_mostly_upper(part1) and not _is_mostly_upper(part2):
				normalized = f"{part2} {part1}"
			else:
				normalized = f"{part1} {part2}"

			names.append(normalized)

	return names


def scan_markdown_folder(input_dir: Path) -> Counter[str]:
	"""
	Parcourt récursivement un dossier à la recherche de fichiers Markdown
	et compte les occurrences de chaque nom/prénom trouvé.
	
	Args:
		input_dir (Path): Le dossier contenant les fichiers .md.
		
	Returns:
		Counter[str]: Un compteur des occurrences par nom/prénom.
	"""
	counts: Counter[str] = Counter()

	for md_file in input_dir.rglob("*.md"):
		try:
			content = md_file.read_text(encoding="utf-8", errors="ignore")
		except Exception:
			continue

		people = extract_person_names_from_text(content)
		counts.update(people)

	return counts


def write_output(output_file: Path, counts: Counter[str]) -> None:
	"""
	Écrit les résultats de l'extraction dans un fichier TSV (Tab-Separated Values).
	
	Args:
		output_file (Path): Le chemin du fichier de destination.
		counts (Counter[str]): Le compteur contenant les résultats.
	"""
	output_file.parent.mkdir(parents=True, exist_ok=True)

	with output_file.open("w", encoding="utf-8") as f:
		f.write("Nom Prénom\tOccurrences\n")
		f.write("--------------------------------\n")
		for name, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
			f.write(f"{name}\t{n}\n")


def main() -> None:
	project_root = Path(__file__).resolve().parents[1]
	default_input = project_root / "data" / "docling_markdown"
	default_output = project_root / "data" / "noms_prenoms.txt"

	parser = argparse.ArgumentParser(description="Extraction des noms/prénoms depuis des fichiers .md")
	parser.add_argument("--input", type=Path, default=default_input, help="Dossier racine contenant les .md")
	parser.add_argument("--output", type=Path, default=default_output, help="Fichier .txt de sortie")
	args = parser.parse_args()

	if not args.input.exists():
		raise FileNotFoundError(f"Dossier introuvable: {args.input}")

	counts = scan_markdown_folder(args.input)
	write_output(args.output, counts)

	print(f"Fait: {len(counts)} noms/prénoms uniques trouvés")
	print(f"Sortie: {args.output}")


if __name__ == "__main__":
	main()
