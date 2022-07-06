"""
Ressource fournie par OpenClassRoom pour le sujet/projet
2022-06-28:
    - modification pour utiliser la classe Goban surchargée qui implémente la solution
2022-06-30:
    - ajout d'un marqueur pytest pour renseigner au moteur de test qu'un test `test_black_shape_is_not_taken_when_it_has_a_liberty` ne fonctionne pas (mais on sait pourquoi :p)
"""
# from goban import Goban
import pytest

from soluce_mentorat import SolutionMentoratGoban as Goban


def test_white_is_taken_when_surrounded_by_black():
    goban = Goban(
        [
            ".#.",
            "#o#",
            ".#.",
        ]
    )

    assert goban.is_taken(1, 1) is True


def test_white_is_not_taken_when_it_has_a_liberty():
    goban = Goban(
        [
            "...",
            "#o#",
            ".#.",
        ]
    )

    assert goban.is_taken(1, 1) is False


def test_black_shape_is_taken_when_surrounded():
    goban = Goban(
        [
            "oo.",
            "##o",
            "o#o",
            ".o.",
        ]
    )

    assert goban.is_taken(0, 1) is True
    assert goban.is_taken(1, 1) is True
    assert goban.is_taken(1, 2) is True


# [XFail: mark test functions as expected to fail](https://docs.pytest.org/en/7.1.x/how-to/skipping.html#reason-parameter)
@pytest.mark.xfail(reason="La récursivité n'est pas encore implémentée")
def test_black_shape_is_not_taken_when_it_has_a_liberty():
    goban = Goban(
        [
            "oo.",
            "##.",
            "o#o",
            ".o.",
        ]
    )

    assert goban.is_taken(0, 1) is False
    assert goban.is_taken(1, 1) is False
    assert goban.is_taken(1, 2) is False


def test_more_complex_black_shape_is_taken():
    goban = Goban(
        [
            "..oo..",
            ".o##oo",
            "o#o###",
            "o###oo",
            ".ooo.."
        ]
    )

    assert goban.is_taken(2, 1) is True
    assert goban.is_taken(5, 2) is True
    assert goban.is_taken(3, 3) is True

def test_more_complex_black_shape_is_not_taken():
    goban = Goban(
        [
            "..oo..",
            ".o##oo",
            ".#o###",
            "o###oo",
            ".ooo.."
        ]
    )

    assert goban.is_taken(2, 1) is False
    assert goban.is_taken(5, 2) is False
    assert goban.is_taken(3, 3) is False


def test_square_shape_is_taken():
    goban = Goban(
        [
            "oo.",
            "##o",
            "##o",
            "oo.",
        ]
    )

    assert goban.is_taken(0, 1) is True
    assert goban.is_taken(0, 2) is True
    assert goban.is_taken(1, 1) is True
    assert goban.is_taken(1, 2) is True
