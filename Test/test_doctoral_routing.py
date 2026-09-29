#!/usr/bin/env python3
"""Test de validation du routage doctoral et de non-régression RAC."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from RAC.RAC import (
    ContactRAG,
    LAB_TO_ED_MAPPING,
    ED_ALIASES,
    inject_ecole_doctorale,
    _detect_laboratory_or_ed_in_text,
    DEFAULT_CONTACT_ROLE_PATH,
)

def test_mappings_and_detection():
    print("=== Test 1: Mappings et détection de labo/ED ===")
    assert _detect_laboratory_or_ed_in_text("Comment s'inscrire au labo BBV ?") == "bbv"
    assert _detect_laboratory_or_ed_in_text("Financement pour le laboratoire GREMAN") == "greman"
    assert _detect_laboratory_or_ed_in_text("Je suis à l'ED 549") == "SSBCV"
    assert _detect_laboratory_or_ed_in_text("Mon école doctorale est MIPTIS") == "MIPTIS"
    assert _detect_laboratory_or_ed_in_text("Quels types de financement de thèse existent ?") is None
    print("✓ Détection textuelle OK")

def test_doctoral_resolution():
    print("=== Test 2: Résolution des contacts doctoraux ===")
    rac = ContactRAG.__new__(ContactRAG)
    from RAC.RAC import ContactRoleIndex
    rac.contact_index = ContactRoleIndex(DEFAULT_CONTACT_ROLE_PATH)

    # 1. ETUDES_DOCTORALES
    # SST: BBV, GREMAN, LIFAT -> Elysa Ragot
    for lab in ["bbv", "greman", "lifat", "ED 549", "EMSTU", "MIPTIS"]:
        contact, target_file = rac._resolve_doctoral_contact("ETUDES_DOCTORALES", lab)
        assert contact is not None, f"Failed for {lab}"
        assert contact.contact_name == "Elysa Ragot", f"Expected Elysa Ragot for {lab}, got {contact.contact_name}"
        assert contact.contact_email == "elysa.ragot@univ-tours.fr"
        assert target_file == "gestionnaire études doctorales SST.txt"

    # SHS: CESR, CITERES -> Christèle Gaudron-Bredif
    for lab in ["cesr", "citeres", "H&L", "SSTED", "ED 616", "ED 617"]:
        contact, target_file = rac._resolve_doctoral_contact("ETUDES_DOCTORALES", lab)
        assert contact is not None, f"Failed for {lab}"
        assert contact.contact_name == "Christele Gaudron-Bredif", f"Expected Christele Gaudron-Bredif for {lab}, got {contact.contact_name}"
        assert contact.contact_email == "gaudron@univ-tours.fr"
        assert target_file == "Etude doctorale2.txt"

    # 2. ECOLES_DOCTORALES
    # SSBCV, SSTED: BBV, CITERES -> Lucie Primault
    for lab in ["bbv", "citeres", "ED 549", "SSBCV", "ED 617", "SSTED"]:
        contact, target_file = rac._resolve_doctoral_contact("ECOLES_DOCTORALES", lab)
        assert contact is not None, f"Failed for {lab}"
        assert "Lucie" in contact.contact_name, f"Expected Lucie Primault for {lab}, got {contact.contact_name}"
        assert contact.contact_email == "lucie.primault@univ-tours.fr"
        assert target_file == "EcoleDoctorale2.txt"

    # EMSTU, MIPTIS, H&L: GREMAN, LIFAT, CESR -> Marie Clermonte
    for lab in ["greman", "lifat", "cesr", "ED 552", "EMSTU", "ED 551", "MIPTIS", "ED 616", "H&L"]:
        contact, target_file = rac._resolve_doctoral_contact("ECOLES_DOCTORALES", lab)
        assert contact is not None, f"Failed for {lab}"
        assert "Marie" in contact.contact_name, f"Expected Marie Clermonte for {lab}, got {contact.contact_name}"
        assert contact.contact_email == "marie.clermonte@univ-tours.fr"
        assert target_file == "EcoleDoctorale.txt"

    print("✓ Résolution de tous les contacts doctoraux OK")

def test_full_rac_queries():
    print("=== Test 3: Requêtes réelles via RAC.ask ===")
    rac = ContactRAG()

    # Requête 1: Financement de thèse sans labo (2 tours)
    print("\n[Tour 1: Financement sans labo]")
    res1 = rac.ask("quels types de financement de thèse existent ?", session_id="test_sess_1")
    print(f"Tag: {res1.routing_tag}")
    print(f"Final answer: {res1.final_answer}")
    assert res1.routing_tag == "ECOLES_DOCTORALES"
    assert "Merci d'indiquer l'acronyme de votre laboratoire" in res1.final_answer
    assert rac.is_pending("test_sess_1")

    print("\n[Tour 2: Réponse labo 'LIFAT']")
    res2 = rac.ask("LIFAT", session_id="test_sess_1")
    print(f"Tag: {res2.routing_tag}")
    print(f"Contact: {res2.contact.contact_name} <{res2.contact.contact_email}>")
    print(f"Fichier: {res2.selected_file}")
    assert res2.routing_tag == "ECOLES_DOCTORALES"
    assert "Marie" in res2.contact.contact_name
    assert res2.contact.contact_email == "marie.clermonte@univ-tours.fr"
    assert res2.selected_file == "EcoleDoctorale.txt"
    assert not rac.is_pending("test_sess_1")

    # Requête 2: Jury de thèse sans labo (2 tours)
    print("\n[Tour 1: Jury sans labo]")
    res3 = rac.ask("Mon jury de thèse est-il valide ?", session_id="test_sess_2")
    print(f"Tag: {res3.routing_tag}")
    print(f"Final answer: {res3.final_answer}")
    assert res3.routing_tag == "ETUDES_DOCTORALES"
    assert "Merci d'indiquer l'acronyme de votre laboratoire" in res3.final_answer
    assert rac.is_pending("test_sess_2")

    print("\n[Tour 2: Réponse labo 'BBV']")
    res4 = rac.ask("BBV", session_id="test_sess_2")
    print(f"Tag: {res4.routing_tag}")
    print(f"Contact: {res4.contact.contact_name} <{res4.contact.contact_email}>")
    print(f"Fichier: {res4.selected_file}")
    assert res4.routing_tag == "ETUDES_DOCTORALES"
    assert res4.contact.contact_name == "Elysa Ragot"
    assert res4.contact.contact_email == "elysa.ragot@univ-tours.fr"
    assert res4.selected_file == "gestionnaire études doctorales SST.txt"
    assert not rac.is_pending("test_sess_2")

    # Requête 3: Question doctorale avec labo direct en 1 tour
    print("\n[1 Tour direct: Inscription avec labo BBV dans la question]")
    res5 = rac.ask("Comment m'inscrire en thèse au labo BBV et qui contacter ?", session_id="test_sess_3")
    print(f"Tag: {res5.routing_tag}")
    print(f"Contact: {res5.contact.contact_name} <{res5.contact.contact_email}>")
    print(f"Fichier: {res5.selected_file}")
    assert res5.routing_tag == "ETUDES_DOCTORALES"
    assert res5.contact.contact_name == "Elysa Ragot"
    assert res5.contact.contact_email == "elysa.ragot@univ-tours.fr"
    assert not rac.is_pending("test_sess_3")

    # Requête 4: Non-régression modification projet (AFRV -> SPIV)
    print("\n[Non-régression: Modification budget CEPR]")
    res6 = rac.ask("Je voudrais modifier le budget prévu sur mon projet (Laboratoire: CEPR)", session_id="test_sess_4")
    print(f"Tag: {res6.routing_tag}")
    print(f"Contact: {res6.contact.contact_name} <{res6.contact.contact_email}>")
    assert res6.routing_tag == "SPIV"
    assert res6.contact.contact_name == "Claude-Emmanuel Boudet"

    rac.close()
    print("\n✓ Tous les tests Full RAC passés avec succès !")

if __name__ == "__main__":
    test_mappings_and_detection()
    test_doctoral_resolution()
    test_full_rac_queries()
