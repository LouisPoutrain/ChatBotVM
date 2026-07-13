from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class LaboratoireAntenne:
    """
    Représente la correspondance entre un laboratoire et son antenne financière (AFRV).
    """
    cf: str
    acronyme: str
    structure: str
    antenne_referente: str
    responsable_af: str


TABLE_DATA: list[LaboratoireAntenne] = [
    LaboratoireAntenne("R4AA", "CETHIS", "Centre Tourangeau d'Histoire et étude des Sources", "AF ASH / af.ash@univ-tours.fr", "Dominique de Gryse"),
    LaboratoireAntenne("R4AC", "CERCA", "CEntre de Recherches sur la Cognition et l'Apprentissage", "AF ASH / af.ash@univ-tours.fr", "Dominique de Gryse"),
    LaboratoireAntenne("R4AD", "INTRU", "Interactions, Transferts, Ruptures artistiques et culturels", "AF ASH / af.ash@univ-tours.fr", "Dominique de Gryse"),
    LaboratoireAntenne("R4AE", "PAVEA", "Psychologie des Ages de la Vie et Adaptation", "AF ASH / af.ash@univ-tours.fr", "Dominique de Gryse"),
    LaboratoireAntenne("R4AF", "IUF A", "Institut Universitaire de France Arts", "AF ASH / af.ash@univ-tours.fr", "Dominique de Gryse"),
    LaboratoireAntenne("R4AG", "QUALIPSY", "Qualité de vie et Psychologie au travail", "AF ASH / af.ash@univ-tours.fr", "Dominique de Gryse"),
    LaboratoireAntenne("R4CA", "CESR", "Centre d'Etudes Supérieures de la Renaissance", "AF CESR / afcesr@univ-tours.fr", "Alexandra Magne"),
    LaboratoireAntenne("R4CB", "IUF CESR", "Institut Universitaire de France CESR -", "AF CESR / afcesr@univ-tours.fr", "Alexandra Magne"),
    LaboratoireAntenne("R4CC", "FESMAR", "Fédération des études supérieures du Moyen-äge et de la renaissance", "AF CESR / afcesr@univ-tours.fr", "Alexandra Magne"),
    LaboratoireAntenne("R4DB", "VALLOREM", "VAL de LOire REcherche en Management", "AF Droit / antenne.financiere.droit@univ-tours.fr", "Patricia Saget"),
    LaboratoireAntenne("R4DD", "CITERES", "Cités, TERritoires, Environnement et Sociétés", "AFRV Citeres Cetu MSH / afrv.citeres@univ-tours.fr", "Karine Latouche"),
    LaboratoireAntenne("R4DG", "IUF DROIT", "IUF DIANE ROMAN", "AF Droit / antenne.financiere.droit@univ-tours.fr", "Patricia Saget"),
    LaboratoireAntenne("RDH", "IUF CITERES", "IUF CITERES", "AFRV Citeres Cetu MSH / afrv.citeres@univ-tours.fr", "Karine Latouche"),
    LaboratoireAntenne("R4DI", "IRJI", "Institut de Recherches Juridiques Interdisciplinaires", "AF Droit / antenne.financiere.droit@univ-tours.fr", "Patricia Saget"),
    LaboratoireAntenne("R4DL", "LEO", "Laboratoire d'Economie d'Orléans", "AF Droit / antenne.financiere.droit@univ-tours.fr", "Patricia Saget"),
    LaboratoireAntenne("R4EB", "LaMé", "Laboratoire de Mécanique Gabriel Lamé", "AF EPU / af.polytech@univ-tours.fr", "Anne Galopin"),
    LaboratoireAntenne("R4EC", "LIFAT", "Laboratoire d'Informatique Fondamentale et Appliquée de Tours", "AF EPU / af.polytech@univ-tours.fr", "Anne Galopin"),
    LaboratoireAntenne("R4EF", "ICVL", "Fédération des informaticiens ICVL", "AF EPU / af.polytech@univ-tours.fr", "Anne Galopin"),
    LaboratoireAntenne("R4LA", "ICD", "Interactions Culturelles et Discursives", "AF Lettres et langues / afll@univ-tours.fr", "Véronique Siron-Perrin"),
    LaboratoireAntenne("R4LD", "DYNADIV", "DYNAMiques et enjeux de la DIVersité linguistique et culturelle", "AF Lettres et langues / afll@univ-tours.fr", "Véronique Siron-Perrin"),
    LaboratoireAntenne("R4LF", "LLL", "Laboratoire Ligérien de Linguistique", "AF Lettres et langues / afll@univ-tours.fr", "Véronique Siron-Perrin"),
    LaboratoireAntenne("R4MA", "I-Brain", "I-BRAIN", "AFRV médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MB", "N2COX", "Nutrition, Croissance et Cancer", "AFRV médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MC", "IUF MEDECINE", "IUF C.BELZUNG", "AFRV médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MD", "MAVIVHE", "Morphogénèse et Antigénicité du VIH et des Virus des Hépatites", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4ME", "ISCHEMIA", "Transplantation, Immunologie et Inflammation", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MH", "EES", "Education Ethique et santé", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MJ", "IUF SR", "IUF S.ROGER", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MK", "SPHERE", "methodS in Patient-centered outcomes and HEalth ResEarch", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4ML", "CEEA", "Comité éthique expérimentation animale", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MS", "CEPR", "Centre d'Etudes des Pathologies Respiratoires", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4MV", "CIC", "Centre d'investigation Clinique", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4PA", "ISP", "Infectiologie et Santé Publique", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4PB", "BBV", "Biomolécules et Biotechnologies Végétales", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4PC", "CBM - NMNS", "Nanomédicaments et nanosondes", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4PS", "SIMBA", "Synthèse et Isolement de Molécules BioActives", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4SA", "BOA", "Biologie des Oiseaux et Aviculture", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4SB", "PRC", "Physiologie de la Reproduction et des Comportements", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4SD", "IRBI", "Institut de Recherche sur la Biologie de l'Insecte", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4SE", "IDP", "Institut Denis Poisson", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4SF", "GEHCO", "Géo-hydrosystèmes continentaux", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4SJ", "PCM2E", "Physico-Chimie des Matériaux et des Electrolytes pour l'Energie", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4TA", "PRIM", "Pratiques et Ressources de l'Information et des Médiations", "AF IUT / servicefinancier-iut@listes.univ-tours.fr", "Stéphanie Chican"),
    LaboratoireAntenne("R4VB", "CETU ELMIS", "ELMIS", "AFRV Citeres Cetu MSH / cetu@univ-tours.fr", "Karine Latouche"),
    LaboratoireAntenne("R4VC", "CETU ETICS", "ETICS", "AFRV Citeres Cetu MSH / cetu@univ-tours.fr", "Karine Latouche"),
    LaboratoireAntenne("R4VD", "CETU INNOPHYT", "INNOPHYT", "AFRV Citeres Cetu MSH / cetu@univ-tours.fr", "Karine Latouche"),
    LaboratoireAntenne("R4VE", "CETU ILIAD 3", "CETU ILIAD 3", "AF EPU / af.polytech@univ-tours.fr", "Anne Galopin"),
    LaboratoireAntenne("R4VY", "PUFR", "Presses universitaires François Rabelais", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4WA", "CERTEM", "CERTEM", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4WB", "CEROC", "CEROC", "AF EPU / af.polytech@univ-tours.fr", "Anne Galopin"),
    LaboratoireAntenne("R4WD", "CERRP", "CERRP", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4WE", "CERMEL", "CERMEL", "AF EPU / af.polytech@univ-tours.fr", "Anne Galopin"),
    LaboratoireAntenne("R4WG", "PIXANIM", "PIXANIM", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4XC", "PST ASB", "Analyse des Systèmes Biologiques", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4XD", "PST A", "Animaleries", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4XG", "MSH", "Maison des Sciences de l'Homme Val de loire", "AFRV Citeres Cetu MSH / cetu@univ-tours.fr", "Karine Latouche"),
    LaboratoireAntenne("R4XH", "", "Fédération Neuroimagerie fonctionnelle : de l'image à la fonction", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4XI", "FERI", "Fédération Agents infectieux, Immunité et thérapies", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4XJ", "CASCIMODOT", "Calcul scientifique et modélisation Orléans et Tours", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4XK", "SAPS", "Science avec et pour la société", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4YA", "C-VALO", "", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4ZB", "", "Relations entreprise (dont pôles de compétitivité)", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4ZC", "ED", "Ecoles doctorales", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4ZE", "", "Labex MabImprove", "AFRV Médecine / afrvm@univ-tours.fr", "Isabelle Thurmel"),
    LaboratoireAntenne("R4ZG", "GREMAN", "GREMAN - Matériaux, microélectronique, acoustique, nanotechnologies", "AFRV Sciences-Pharmacie / afrvgrandmont@univ-tours.fr", "Isabelle Bronchart"),
    LaboratoireAntenne("R4ZP", "PUI", "Pôle Universitaire d'Innovation", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4ZV", "", "Brevets Recherche", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
    LaboratoireAntenne("R4ZZ", "", "Service général (chercheurs invités)", "AFRV Centrale / afrvcentrale@univ-tours.fr", "Sylvain Riviere"),
]


def to_dicts(rows: list[LaboratoireAntenne]) -> list[dict[str, str]]:
    return [asdict(row) for row in rows]


def build_indexes(rows: list[LaboratoireAntenne]) -> dict[str, dict[str, list[dict[str, str]]]]:
    by_cf: dict[str, dict[str, str]] = {}
    by_antenne: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_responsable: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in rows:
        row_dict = asdict(row)
        if row.cf:
            by_cf[row.cf] = row_dict
        by_antenne[row.antenne_referente].append(row_dict)
        by_responsable[row.responsable_af].append(row_dict)

    return {
        "by_cf": by_cf,
        "by_antenne": dict(by_antenne),
        "by_responsable": dict(by_responsable),
    }


def export_json(path: Path, rows: list[LaboratoireAntenne]) -> None:
    payload: dict[str, Any] = {
        "rows": to_dicts(rows),
        "indexes": build_indexes(rows),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Expose le tableau des antennes financières sous forme de structure Python.")
    parser.add_argument("--output-json", type=Path, default=None, help="Export JSON optionnel des données structurées.")
    args = parser.parse_args()

    if args.output_json is not None:
        export_json(args.output_json, TABLE_DATA)
        print(f"JSON exporte: {args.output_json}")
        return

    print(f"Lignes chargees: {len(TABLE_DATA)}")
    print("Exemple de structure Python:")
    print(to_dicts(TABLE_DATA[:2]))


if __name__ == "__main__":
    main()