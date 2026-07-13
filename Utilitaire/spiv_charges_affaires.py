from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ChargeAffairesSPIV:
    """
    Représente un chargé d'affaires pour le SPIV (Service Partenariat et Innovation).
    
    Attributes:
        nom (str): Nom complet du chargé d'affaires.
        email (str): Adresse email de contact.
        thematique (str): Domaine ou thématique de recherche (ex: 'Santé').
        laboratoires (list[str]): Liste des acronymes de laboratoires gérés.
    """
    nom: str
    email: str
    thematique: str
    laboratoires: list[str]


@dataclass(frozen=True)
class ChargeAffairesEurope:
    """
    Représente un contact Europe pour la DRV.
    
    Attributes:
        nom (str): Nom complet.
        email (str): Adresse email.
    """
    nom: str
    email: str


CHARGES_AFFAIRES_SPIV: list[ChargeAffairesSPIV] = [
    ChargeAffairesSPIV(
        nom="Mélanie Fauconnier",
        email="melanie.fauconnier@univ-tours.fr",
        thematique="Sciences humaines et sociales",
        laboratoires=["CeRCA", "CESR", "CeTHIS", "LEO", "LLL", "PAVeA", "Qualipsy", "VALLOREM"],
    ),
    ChargeAffairesSPIV(
        nom="Justine Gillet",
        email="justine.gillet@univ-tours.fr",
        thematique="Energie et Matériaux",
        laboratoires=["GREMAN", "LIFAT", "LaMé", "PCM2E", "CERMEL", "CERTEM", "CEROC"],
    ),
    ChargeAffairesSPIV(
        nom="Laurine Drugat",
        email="laurine.drugat@univ-tours.fr",
        thematique="Sciences de la vie, sciences sociales",
        laboratoires=["CITERES", "BBV", "GEHCO", "UAR METIS"],
    ),
    ChargeAffairesSPIV(
        nom="Helène Jullien",
        email="Hélène.jullien@univ-tours.fr",
        thematique="Santé",
        laboratoires=["ISCHEMIA", "ISP", "MAVIVHe", "N2COx", "PST ASB", "SIMBA"],
    ),
    ChargeAffairesSPIV(
        nom="Claude-Emmanuel Boudet",
        email="cboudet@univ-tours.fr",
        thematique="Santé",
        laboratoires=["CEPR U 1100", "SPHERE", "PST Animalerie"],
    ),
]


CHARGES_AFFAIRES_EUROPE: list[ChargeAffairesEurope] = [
    ChargeAffairesEurope(nom="Franziska Metzinger", email="franziska.metzinger@univ-tours.fr"),
    ChargeAffairesEurope(nom="Marie Agnès Benoît", email="marie-agnes.benoit@univ-tours.fr"),
]


def to_dicts(rows: list[Any]) -> list[dict[str, Any]]:
    """Convertit une liste de dataclasses en liste de dictionnaires."""
    return [asdict(row) for row in rows]


def build_indexes(rows: list[ChargeAffairesSPIV]) -> dict[str, dict[str, Any]]:
    """
    Construit des index inversés pour retrouver rapidement un chargé d'affaires SPIV
    par nom, par thématique ou par acronyme de laboratoire.
    """
    by_nom: dict[str, dict[str, Any]] = {}
    by_thematique: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_laboratoire: dict[str, dict[str, Any]] = {}

    for row in rows:
        row_dict = asdict(row)
        by_nom[row.nom] = row_dict
        by_thematique[row.thematique].append(row_dict)
        for laboratoire in row.laboratoires:
            by_laboratoire[laboratoire] = row_dict

    return {
        "by_nom": by_nom,
        "by_thematique": dict(by_thematique),
        "by_laboratoire": by_laboratoire,
    }


def export_json(path: Path) -> None:
    """Exporte les données des chargés d'affaires (SPIV et Europe) et leurs index au format JSON."""
    payload: dict[str, Any] = {
        "charges_affaires_spiv": to_dicts(CHARGES_AFFAIRES_SPIV),
        "charges_affaires_europe": to_dicts(CHARGES_AFFAIRES_EUROPE),
        "indexes": {
            "spiv": build_indexes(CHARGES_AFFAIRES_SPIV),
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Expose le tableau SPIV sous forme de structure Python exploitable.")
    parser.add_argument("--output-json", type=Path, default=None, help="Export JSON optionnel des données.")
    args = parser.parse_args()

    if args.output_json is not None:
        export_json(args.output_json)
        print(f"JSON exporte: {args.output_json}")
        return

    print(f"Chargés d'affaires SPIV: {len(CHARGES_AFFAIRES_SPIV)}")
    print(f"Contacts Europe: {len(CHARGES_AFFAIRES_EUROPE)}")
    print(to_dicts(CHARGES_AFFAIRES_SPIV[:1]))


if __name__ == "__main__":
    main()