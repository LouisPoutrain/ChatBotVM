from __future__ import annotations

import argparse
import csv
import json
import logging
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import numpy as np
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# ==============================================================================
# SEMANTIC SIMILARITY WITH EMBEDDINGS
# ==============================================================================

class SemanticEmbedder:
	"""Gestionnaire d'embeddings sémantiques avec SentenceTransformer."""
	
	_instance = None
	
	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			logger.info("Initialisation du modèle d'embedding (intfloat/multilingual-e5-large)...")
			cls._instance.model = SentenceTransformer("intfloat/multilingual-e5-large")
		return cls._instance
	
	def encode(self, texts: Sequence[str]) -> np.ndarray:
		"""Encode une liste de textes en vecteurs.
		
		Args:
			texts: Séquence de chaînes à encoder.
			
		Returns:
			Matrice numpy de shape (len(texts), 1024).
		"""
		if not texts:
			return np.array([])
		return self.model.encode(list(texts), convert_to_numpy=True)
	
	def similarity(self, text1: str, text2: str) -> float:
		"""Calcule la similarité cosinus entre deux textes.
		
		Args:
			text1, text2: Chaînes à comparer.
			
		Returns:
			Score de 0 à 1 (1 = identique sémantiquement).
		"""
		if not text1 or not text2:
			return 1.0 if (not text1 and not text2) else 0.0
		embeddings = self.encode([text1, text2])
		# Calcul de la similarité cosinus avec numpy
		norm1 = np.linalg.norm(embeddings[0])
		norm2 = np.linalg.norm(embeddings[1])
		if norm1 == 0 or norm2 == 0:
			return 0.0
		return float(np.dot(embeddings[0], embeddings[1]) / (norm1 * norm2))


def _group_by_semantic_similarity(choices: Sequence[str], threshold: float = 0.85) -> dict[int, list[str]]:
	"""Groupe les réponses par similarité sémantique.
	
	Args:
		choices: Réponses à grouper.
		threshold: Seuil de similarité (0-1) pour considérer deux textes comme équivalents.
		
	Returns:
		Dict avec groupe_id → liste des réponses similaires.
	"""
	if not choices:
		return {}
	
	embedder = SemanticEmbedder()
	normalized_choices = [_normalize_choice(c) for c in choices]
	embeddings = embedder.encode(normalized_choices)
	
	if len(embeddings) == 0:
		return {}
	
	groups: dict[int, list[str]] = defaultdict(list)
	assigned = set()
	group_id = 0
	
	for i, choice in enumerate(normalized_choices):
		if i in assigned:
			continue
		
		groups[group_id].append(choice)
		assigned.add(i)
		
		# Chercher tous les textes similaires
		for j in range(i + 1, len(normalized_choices)):
			if j in assigned:
				continue
			
			# Calcul de la similarité cosinus
			norm_i = np.linalg.norm(embeddings[i])
			norm_j = np.linalg.norm(embeddings[j])
			if norm_i > 0 and norm_j > 0:
				sim = float(np.dot(embeddings[i], embeddings[j]) / (norm_i * norm_j))
				if sim >= threshold:
					groups[group_id].append(normalized_choices[j])
					assigned.add(j)
		
		group_id += 1
	
	return groups
class JudgeTrial:
	question_id: str
	choice: str
	trial_id: str | None = None


def _normalize_choice(choice: Any) -> str:
	text = "" if choice is None else str(choice)
	return " ".join(text.strip().split())


def _as_question_groups(groups: Mapping[Any, Sequence[Any]]) -> list[list[str]]:
	normalized_groups: list[list[str]] = []
	for trials in groups.values():
		normalized = [_normalize_choice(choice) for choice in trials if _normalize_choice(choice)]
		if normalized:
			normalized_groups.append(normalized)
	return normalized_groups


def _majority_choice(choices: Sequence[Any]) -> str:
	normalized = [_normalize_choice(choice) for choice in choices if _normalize_choice(choice)]
	if not normalized:
		return ""
	return Counter(normalized).most_common(1)[0][0]


def repetition_stability(groups: Sequence[Sequence[Any]], use_semantic: bool = True, threshold: float = 0.85) -> float:
	"""Compute the RS metric as the average majority vote ratio per question.
	
	Args:
		groups: Séquence de listes de réponses par question.
		use_semantic: Si True, utilise la similarité sémantique; sinon, comparaison exacte.
		threshold: Seuil de similarité pour le groupage sémantique (0-1).
		
	Returns:
		Score RS entre 0 et 1.
	"""
	ratios: list[float] = []

	for trials in groups:
		normalized_trials = [_normalize_choice(choice) for choice in trials if _normalize_choice(choice)]
		if not normalized_trials:
			continue

		if use_semantic:
			# Grouper par similarité sémantique
			semantic_groups = _group_by_semantic_similarity(normalized_trials, threshold=threshold)
			group_sizes = [len(group) for group in semantic_groups.values() if group]
			if group_sizes:
				ratios.append(max(group_sizes) / len(normalized_trials))
		else:
			# Comparaison exacte (original)
			counts = Counter(normalized_trials)
			ratios.append(max(counts.values()) / len(normalized_trials))

	return sum(ratios) / len(ratios) if ratios else 0.0


def position_consistency(groups: Sequence[Sequence[Any]], use_semantic: bool = True, threshold: float = 0.85) -> float:
	"""Compute the PC metric as the fraction of questions with identical/similar choices across permutations.
	
	Args:
		groups: Séquence de listes de réponses par question.
		use_semantic: Si True, utilise la similarité sémantique; sinon, comparaison exacte.
		threshold: Seuil de similarité pour le groupage sémantique (0-1).
		
	Returns:
		Score PC entre 0 et 1.
	"""
	decisions: list[int] = []

	for trials in groups:
		normalized_trials = [_normalize_choice(choice) for choice in trials if _normalize_choice(choice)]
		if not normalized_trials:
			continue

		if use_semantic:
			# Grouper par similarité sémantique
			semantic_groups = _group_by_semantic_similarity(normalized_trials, threshold=threshold)
			# Si un seul groupe sémantique, tous les choix sont similaires
			decisions.append(1 if len(semantic_groups) == 1 else 0)
		else:
			# Comparaison exacte (original)
			decisions.append(1 if len(set(normalized_trials)) == 1 else 0)

	return sum(decisions) / len(decisions) if decisions else 0.0


def evaluate_rs_pc(
	repetition_groups: Mapping[Any, Sequence[Any]] | Sequence[Sequence[Any]],
	position_groups: Mapping[Any, Sequence[Any]] | Sequence[Sequence[Any]],
	use_semantic: bool = True,
	threshold: float = 0.85,
) -> dict[str, float]:
	if isinstance(repetition_groups, Mapping):
		repetition_groups = _as_question_groups(repetition_groups)
	if isinstance(position_groups, Mapping):
		position_groups = _as_question_groups(position_groups)

	return {
		"rs": repetition_stability(repetition_groups, use_semantic=use_semantic, threshold=threshold),
		"pc": position_consistency(position_groups, use_semantic=use_semantic, threshold=threshold),
	}


def load_groups_from_json(path: Path) -> tuple[list[list[str]], list[list[str]]]:
	payload = json.loads(path.read_text(encoding="utf-8"))

	if isinstance(payload, dict) and "trials" in payload and isinstance(payload["trials"], list):
		return _groups_from_trials(payload["trials"])

	if isinstance(payload, list):
		repetition_rows = [row for row in payload if str(row.get("metric", "")).lower() in {"rs", "repetition", "repetition_stability"}]
		position_rows = [row for row in payload if str(row.get("metric", "")).lower() in {"pc", "position", "position_consistency"}]
		return _rows_to_groups(repetition_rows), _rows_to_groups(position_rows)

	if not isinstance(payload, dict):
		raise ValueError("Unsupported JSON structure. Expected a dict or list of records.")

	repetition_data = payload.get("repetition", payload.get("rs", []))
	position_data = payload.get("position", payload.get("pc", []))

	return _coerce_group_payload(repetition_data), _coerce_group_payload(position_data)


def _groups_from_trials(trials: Sequence[Mapping[str, Any]]) -> tuple[list[list[str]], list[list[str]]]:
	repetition_groups: dict[tuple[str, str, str], list[tuple[int, str]]] = defaultdict(list)
	per_question_configs: dict[str, dict[tuple[str, str], list[tuple[int, str]]]] = defaultdict(lambda: defaultdict(list))

	for index, trial in enumerate(trials):
		question_key = _normalize_choice(trial.get("question_index", trial.get("question_id", trial.get("question", index))))
		prompt_variant = _normalize_choice(trial.get("prompt_variant", "default")) or "default"
		context_order = _normalize_choice(trial.get("context_order", "preserve")) or "preserve"
		repeat_value = trial.get("repeat_index", trial.get("repeat", index))
		answer = _normalize_choice(trial.get("final_answer", trial.get("answer", trial.get("choice", ""))))

		if not question_key or not answer:
			continue

		try:
			repeat_index = int(repeat_value)
		except Exception:
			repeat_index = index

		repetition_groups[(question_key, prompt_variant, context_order)].append((repeat_index, answer))
		per_question_configs[question_key][(prompt_variant, context_order)].append((repeat_index, answer))

	repetition_payload: list[list[str]] = []
	for items in repetition_groups.values():
		repetition_payload.append([answer for _, answer in sorted(items, key=lambda item: item[0])])

	position_payload: list[list[str]] = []
	for question_key, config_groups in per_question_configs.items():
		ordered_representatives: list[tuple[tuple[str, str], str]] = []
		for config_key, items in sorted(config_groups.items(), key=lambda item: item[0]):
			representatives = [answer for _, answer in sorted(items, key=lambda item: item[0])]
			ordered_representatives.append((config_key, _majority_choice(representatives)))

		question_answers = [answer for _, answer in ordered_representatives if answer]
		if question_answers:
			position_payload.append(question_answers)

	return repetition_payload, position_payload


def _coerce_group_payload(payload: Any) -> list[list[str]]:
	if isinstance(payload, Mapping):
		return _as_question_groups(payload)
	if isinstance(payload, list):
		if not payload:
			return []
		if all(isinstance(item, list) for item in payload):
			return [[_normalize_choice(choice) for choice in item if _normalize_choice(choice)] for item in payload if item]
		if all(isinstance(item, Mapping) for item in payload):
			return _rows_to_groups(payload)
	raise ValueError("Unsupported group payload format.")


def _rows_to_groups(rows: Iterable[Mapping[str, Any]]) -> list[list[str]]:
	grouped: dict[str, list[tuple[int, str]]] = defaultdict(list)

	for index, row in enumerate(rows):
		question_id = _normalize_choice(row.get("question_id", row.get("question", row.get("id", ""))))
		choice = _normalize_choice(row.get("choice", row.get("decision", row.get("answer", ""))))
		if not question_id or not choice:
			continue

		order_value = row.get("order", row.get("trial_id", row.get("permutation_id", index)))
		try:
			order = int(order_value)
		except Exception:
			order = index

		grouped[question_id].append((order, choice))

	return [
		[choice for _, choice in sorted(items, key=lambda item: item[0])]
		for items in grouped.values()
		if items
	]


def load_groups_from_csv(path: Path) -> tuple[list[list[str]], list[list[str]]]:
	with path.open(encoding="utf-8", newline="") as csv_file:
		reader = csv.DictReader(csv_file)
		rows = list(reader)

	if not rows:
		return [], []

	if "metric" in rows[0]:
		repetition_rows = [row for row in rows if str(row.get("metric", "")).lower() in {"rs", "repetition", "repetition_stability"}]
		position_rows = [row for row in rows if str(row.get("metric", "")).lower() in {"pc", "position", "position_consistency"}]
		return _rows_to_groups(repetition_rows), _rows_to_groups(position_rows)

	raise ValueError("CSV files must include a 'metric' column to distinguish RS and PC rows.")


def summarize_metrics(rs_value: float, pc_value: float) -> str:
	return (
		"RS = "
		f"{rs_value:.4f} | "
		"PC = "
		f"{pc_value:.4f}"
	)


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Compute Repetition Stability (RS) and Position Consistency (PC)."
	)
	parser.add_argument("--input", type=Path, required=True, help="JSON or CSV file containing judge outputs.")
	parser.add_argument("--output", type=Path, default=None, help="Optional JSON file for the computed summary.")
	parser.add_argument(
		"--no-semantic",
		action="store_true",
		help="Use exact string matching instead of semantic similarity (default: use semantic similarity)."
	)
	parser.add_argument(
		"--threshold",
		type=float,
		default=0.85,
		help="Semantic similarity threshold (0-1) for grouping similar responses (default: 0.85)."
	)
	args = parser.parse_args()

	if not args.input.exists():
		raise FileNotFoundError(f"Input file not found: {args.input}")

	if args.input.suffix.lower() == ".json":
		repetition_groups, position_groups = load_groups_from_json(args.input)
	elif args.input.suffix.lower() == ".csv":
		repetition_groups, position_groups = load_groups_from_csv(args.input)
	else:
		raise ValueError("Unsupported input format. Use .json or .csv.")

	use_semantic = not args.no_semantic
	metrics = evaluate_rs_pc(
		repetition_groups,
		position_groups,
		use_semantic=use_semantic,
		threshold=args.threshold
	)

	mode = "exact match" if not use_semantic else f"semantic (threshold={args.threshold})"
	print(f"Mode: {mode}")
	print(summarize_metrics(metrics["rs"], metrics["pc"]))

	if args.output:
		args.output.parent.mkdir(parents=True, exist_ok=True)
		metrics["mode"] = mode
		args.output.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
	main()
