import pytest
from MMORPG import Personnage, Guerrier, Mage, Joueur

def test_perso():
    p = Personnage("Armin")
    assert p.nom == "Armin"
    assert p.niveau == 1
    assert p.pv == 1
    assert p.init == 1

def test_niveau():
    p = Personnage("Armin", niveau=1000)
    assert p.pseudo == "Armin"
    assert p.niveau == 1000
    assert p.pv == 1
    assert p.init == 1

def test_degats():
    p = Personnage("Armin", niveau=1000)
    assert p.degats() == 5

def test_egalite():
    p1 = Personnage("Armin", niveau=1000)
    p2 = Personnage("Evan", niveau=1000)
    p3 = Personnage("Louis", niveau=35)
    p4 = Personnage("Hero", niveau=2)

    assert p1 == p2
    assert p1 != p3
    assert p1 != p4

def test_perso_soigner():
    p = Personnage("Armin", niveau=100)
    p.soigner()
    assert p.pv == 100