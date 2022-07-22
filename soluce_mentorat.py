"""
2022-06-28:
    - ✔️ stratégie simple (non récursive) et directe pour passer les premiers tests unitaires
    - ✔ par "chance" le test `test_square_shape_is_taken`,
        car il n'y aucune liberté pour la forme (aucune de ces pièces)
        donc la récursivité n'est pas nécessaire
    - ❌ le test unitaire `test_black_shape_is_not_taken_when_it_has_a_liberty`
        sur la forme avec une liberté sur une des pièces ne fonctionne pas (normal)
"""
from typing import List, Optional

from goban import Goban, Status


class SolutionMentoratGoban(Goban):
    def __init__(self, goban: List[str]):
        super().__init__(goban)

    def is_taken(
        self, x: int, y: int, historic_of_positions: Optional[list] = None
    ) -> bool:
        """
        si la pierre à une position x, y sur un goban est prise ou pas
        """
        # 1ère étape: ❓ Est ce que la position (x, y) est sur une pierre ou pas ❓
        status_position = self.get_status(x, y)

        if status_position == Status.EMPTY or status_position == Status.OUT:
            return False

        # 2ème étape: ❓ Est une position adjacente est libre ❓
        positions_adjacentes = [
            ((x + 1, y), self.get_status(x + 1, y)),  # position adjacente ➡ droite
            ((x - 1, y), self.get_status(x - 1, y)),  # position adjacente ⬅ gauche
            ((x, y + 1), self.get_status(x, y + 1)),  # position adjacente ⬇ bas
            ((x, y - 1), self.get_status(x, y - 1)),  # position adjacente ⬆ haute
        ]
        if historic_of_positions is None:
            historic_of_positions = []
        historic_of_positions.append((x, y))
        # 🔮 Est ce qu'une position adjacente est libre ❓
        for position_adjacente, status_position_adjacente in positions_adjacentes:
            # ❓ Est ce que la position adjacente est libre ❓
            if status_position_adjacente == Status.EMPTY:
                # ✅ si oui la piece (x, y) n'est pas prise
                return False
            else:
                # ? Est-ce que la pierre adjacente est de la même couleur ?
                if status_position == status_position_adjacente:
                    # [rec] on poursuit la création d'une forme
                    # ? Est ce que la position adjacente est dans l'historique des positions visitées ?
                    if position_adjacente in historic_of_positions:
                        # si Oui => on est déjà passé par là donc on n'y retourne
                        pass
                    else:
                        print(f"recursive call with position: {position_adjacente}")
                        if not self.is_taken(
                            position_adjacente[0],
                            position_adjacente[1],
                            historic_of_positions,
                        ):
                            return False
                else:
                    # c'est une pierre adverse donc la position pour cette direction est prise
                    pass
        # ℹ Toute les positions adjacentes ne sont pas libres (i.e une pierre sur chaque position adjacente)
        print()
        # => on considère la pièce prise
        return True
