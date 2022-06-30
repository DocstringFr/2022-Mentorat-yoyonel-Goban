"""
2022-06-28:
    - ✔️ stratégie simple (non récursive) et directe pour passer les premiers tests unitaires
    - ✔ par "chance" le test `test_square_shape_is_taken`,
        car il n'y aucune liberté pour la forme (aucune de ces pièces)
        donc la récursivité n'est pas nécessaire
    - ❌ le test unitaire `test_black_shape_is_not_taken_when_it_has_a_liberty`
        sur la forme avec une liberté sur une des pièces ne fonctionne pas (normal)
"""
from typing import List

from goban import Goban, Status


class SolutionMentoratGoban(Goban):
    def __init__(self, goban: List[str]):
        super().__init__(goban)

    def is_taken(self, x: int, y: int) -> bool:
        """
        si la pierre à une position x, y sur un goban est prise ou pas
        """
        # 1ère étape: ❓ Est ce que la position (x, y) est sur une pierre ou pas ❓
        status_position = self.get_status(x, y)

        if status_position == Status.EMPTY or status_position == Status.OUT:
            return False

        # 2ème étape: ❓ Est une position adjacente est libre ❓
        status_positions_adjacentes = [
            self.get_status(x + 1, y),  # position adjacente ➡ droite
            self.get_status(x - 1, y),  # position adjacente ⬅ gauche
            self.get_status(x, y + 1),  # position adjacente ⬇ bas
            self.get_status(x, y - 1),  # position adjacente ⬆ haute
        ]
        # 🔮 Est ce qu'une position adjacente est libre ❓
        for status_position_adjacente in status_positions_adjacentes:
            # ❓ Est ce que la position adjacente est libre ❓
            if status_position_adjacente == Status.EMPTY:
                # ✅ si oui la piece (x, y) n'est pas prise
                return False
        # ℹ Toute les positions adjacentes ne sont pas libres (i.e une pierre sur chaque position adjacente)

        # => on considère la pièce prise
        return True
