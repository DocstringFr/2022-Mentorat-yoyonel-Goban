"""
2022-06-28:
    - ✔️ stratégie simple (non récursive) et directe pour passer les premiers tests unitaires
    - ✔ par "chance" le test `test_square_shape_is_taken`,
        car il n'y aucune liberté pour la forme (aucune de ces pièces)
        donc la récursivité n'est pas nécessaire
    - ❌ le test unitaire `test_black_shape_is_not_taken_when_it_has_a_liberty`
        sur la forme avec une liberté sur une des pièces ne fonctionne pas (normal)
"""
from typing import List, Tuple

from goban import Goban, Status


class SolutionMentoratGoban(Goban):
    def __init__(self, goban: List[str]):
        super().__init__(goban)

        self._shape_is_free = False

    def is_taken(self, x: int, y: int, positions: set | None = None) -> bool:
        """
        si la pierre à une position x, y sur un goban est prise ou pas
        """
        # 1ère étape: ❓ Est ce que la position (x, y) est sur une pierre ou pas ❓
        status_position = self.get_status(x, y)

        if status_position in [Status.EMPTY, Status.OUT]:
            return False

        # Initialisation de l'historique des positions testées et de l'état de la forme
        if positions is None:
            positions = {(x, y)}

        # 2ème étape: ❓ Est une position adjacente est libre ❓
        status_positions_adjacentes: List[Tuple[Status, Tuple[int, int]]] = [
            (self.get_status(x + 1, y), (x + 1, y)),  # position adjacente ➡ droite
            (self.get_status(x - 1, y), (x - 1, y)),  # position adjacente ⬅ gauche
            (self.get_status(x, y + 1), (x, y + 1)),  # position adjacente ⬇ bas
            (self.get_status(x, y - 1), (x, y - 1)),  # position adjacente ⬆ haute
        ]
        # 🔮 Est ce qu'une position adjacente est libre ❓
        for status_position_adjacente, position_adjacente in status_positions_adjacentes:
            # ❓ Est ce que la position adjacente est libre ❓
            if status_position_adjacente == Status.EMPTY:
                # ✅ si oui la piece (x, y) est libre et donc la forme est libre
                self._shape_is_free = True
            # ❓ Sinon, est ce que les positions adjacentes de la position actuelle sont libres ❓
            # On test une position adjacente seulement si:
            # - Aucune position libre déjà trouvée (évite de continuer la recherche)
            # - Pas déjà testé
            # - La position actuelle est de la couleur de la position adjacente
            elif not self._shape_is_free and \
                    position_adjacente not in positions and \
                    status_position == status_position_adjacente:
                # Ajout de la position à l'historique
                positions.add((x, y))
                # Appel récursif de la méthode avec nouvelle position et historique des positions testées
                self.is_taken(*position_adjacente, positions=positions)

        # Retourne que la pièce est prise si la forme n'a pas de liberté
        return not self._shape_is_free
