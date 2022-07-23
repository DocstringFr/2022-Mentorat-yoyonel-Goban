"""
Ressource fournie par OpenClassRoom pour le sujet/projet
2022-06-28:
    - modification pour utiliser la classe Goban surchargée qui implémente la solution
2022-06-30:
    - ajout d'un marqueur pytest pour renseigner au moteur de test qu'un test `test_black_shape_is_not_taken_when_it_has_a_liberty` ne fonctionne pas (mais on sait pourquoi :p)
"""
from typing import Type, TypeVar

import pytest

from goban import Goban
from soluce_advanced import SolutionAdvancedGoban as SolutionAdvancedGoban
from soluce_mentorat import SolutionMentoratGoban

# [Subclass in type hinting](https://stackoverflow.com/a/71441339)
U = TypeVar("U", bound=Goban)

SolutionsToTest = (SolutionMentoratGoban, SolutionAdvancedGoban)


@pytest.mark.parametrize("class_object_solution_to_test", SolutionsToTest)
def test_white_is_taken_when_surrounded_by_black(
    class_object_solution_to_test: Type[U],
):
    goban = class_object_solution_to_test(
        [
            ".#.",
            "#o#",
            ".#.",
        ]
    )

    assert goban.is_taken(1, 1) is True


@pytest.mark.parametrize("class_object_solution_to_test", SolutionsToTest)
def test_white_is_not_taken_when_it_has_a_liberty(
    class_object_solution_to_test: Type[U],
):
    goban = class_object_solution_to_test(
        [
            "...",
            "#o#",
            ".#.",
        ]
    )

    assert goban.is_taken(1, 1) is False


@pytest.mark.parametrize("class_object_solution_to_test", SolutionsToTest)
def test_black_shape_is_taken_when_surrounded(class_object_solution_to_test: Type[U]):
    goban = class_object_solution_to_test(
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


@pytest.mark.parametrize("class_object_solution_to_test", SolutionsToTest)
def test_black_shape_is_not_taken_when_it_has_a_liberty(
    class_object_solution_to_test: Type[U],
):
    goban = class_object_solution_to_test(
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


@pytest.mark.parametrize("class_object_solution_to_test", SolutionsToTest)
def test_square_shape_is_taken(class_object_solution_to_test: Type[U]):
    goban = class_object_solution_to_test(
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
