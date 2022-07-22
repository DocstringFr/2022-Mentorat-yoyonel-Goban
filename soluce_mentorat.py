"""
2022-06-28:
    - ✔️ stratégie simple (non récursive) et directe pour passer les premiers tests unitaires
    - ✔ par "chance" le test `test_square_shape_is_taken`,
        car il n'y aucune liberté pour la forme (aucune de ces pièces)
        donc la récursivité n'est pas nécessaire
    - ❌ le test unitaire `test_black_shape_is_not_taken_when_it_has_a_liberty`
        sur la forme avec une liberté sur une des pièces ne fonctionne pas (normal)
"""
from typing import List, Tuple, Union

from goban import Goban, Status


def get_untested_position(historique: dict, change_etat: bool = False) -> Union[Tuple[int, int], None]:
    """
    Récupère une position pas encore testée (état à False)
    et la passe à True si option change_etat

    Args:
        historique: Etat des positions adjacentes à la forme
        change_etat: Option de mise à jour de l'état

    Returns:
        - une position : (x, y)
        - None si aucune position trouvée
    """
    for position_centre, positions_adjacentes in historique.items():
        for position_adjacente, etat in positions_adjacentes.items():
            if not etat:
                if change_etat:
                    historique[position_centre][position_adjacente] = True
                return position_adjacente


class SolutionMentoratGoban(Goban):
    def __init__(self, goban: List[str]):
        super().__init__(goban)

    def is_taken(self, x: int, y: int) -> bool:
        """
        si la pierre à une position x, y sur un goban est prise ou pas
        """
        # 1ère étape: ❓ Est ce que la position (x, y) est sur une pierre ou pas ❓
        status_position_initial = self.get_status(x, y)

        if status_position_initial in [Status.EMPTY, Status.OUT]:
            return False

        # 2ème étape: ❓ Est une position adjacente est libre ❓
        # Initialisation d'un dictionnaire listant les positions adjacentes à tester
        positions = {(x, y): {(x + 1, y): False,
                              (x - 1, y): False,
                              (x, y + 1): False,
                              (x, y - 1): False}}
        # 🔮 Est ce qu'une position adjacente est libre ❓
        while get_untested_position(positions):
            position_a_tester = get_untested_position(positions, True)
            # ❓ Est ce que la position adjacente est libre ❓
            status_position_adjacente = self.get_status(*position_a_tester)
            if status_position_adjacente == Status.EMPTY:
                # ✅ si oui la piece (x, y) n'est pas prise
                return False
            # Sinon, si la position adjacente fait partie de la forme
            # et pas déjà présente dans l'historique
            elif (
                    status_position_adjacente == status_position_initial
                    and position_a_tester not in positions
            ):
                # Position actuelle
                x, y = position_a_tester

                # Détermination des positions adjacentes à la position actuelle
                # et retrait de celles déjà testées
                positions_adjacentes_potentielles = {}
                pos = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                [positions_adjacentes_potentielles.update({(x, y): False}) for (x, y) in pos if (x, y) not in positions]
                new_position = {position_a_tester: positions_adjacentes_potentielles}

                # Ajout de la position actuelle à l'historique avec ses positions adjacentes à tester
                positions.update(new_position)

        # Aucune liberté trouvée → la position/forme n'est pas libre
        return True
