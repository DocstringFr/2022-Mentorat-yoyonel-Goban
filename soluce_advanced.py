from dataclasses import dataclass, astuple
from typing import List

try:
    from typing import Final
except ImportError:
    # https://pypi.org/project/typing-extensions/
    from typing_extensions import Final

from goban import Goban as OpenClassRoom_Goban, Status


# https://docs.python.org/3/library/dataclasses.html#module-dataclasses
@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)


class SolutionAdvancedGoban(OpenClassRoom_Goban):
    # https://docs.python.org/3/library/typing.html#type-aliases
    # https://docs.python.org/3/library/typing.html#typing.Final
    DIR_NEIGHBORS: Final[List[Position]] = [
        Position(i, j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        # https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html
        if abs(i) ^ abs(j)
    ]

    def __init__(self, goban):
        super().__init__(goban)
        self._board_height = len(self.goban)
        self._board_width = len(self.goban[0])
        self._walk_map: List[List[Status]] = []

    def _init_walk_map(self):
        self._walk_map = [
            [Status.EMPTY] * self._board_width for _ in range(self._board_height)
        ]

    def _get_status_on_walk_map(self, position: Position) -> Status:
        return self._walk_map[position.y][position.x]

    def _set_status_on_walk_map(self, position: Position, status: Status):
        self._walk_map[position.y][position.x] = status

    def _recursive_is_taken(self, position: Position, current_status: Status) -> bool:
        # update the walk-map (can be accessed because on Goban::is_taken scope)
        self._set_status_on_walk_map(position, current_status)

        # retrieve all neighbors status
        neighbors_status = [
            # https://docs.python.org/3/library/dataclasses.html#dataclasses.astuple
            self.get_status(*astuple(position + dir_neighbor))
            for dir_neighbor in SolutionAdvancedGoban.DIR_NEIGHBORS
        ]

        # one or more direct neighbors is a free (EMPTY) slot => one freedom available (shape not taken)
        # https://docs.python.org/3/library/functions.html#any
        if any(neighbor_status == Status.EMPTY for neighbor_status in neighbors_status):
            # [optim] early exit
            return False

        # [init] we consider no free mouvement available => shape is taken
        result_is_taken = True
        # loop on each neighbors
        for dir_neighbor, status_neighbor in zip(
            SolutionAdvancedGoban.DIR_NEIGHBORS, neighbors_status
        ):
            # neighbor position
            next_position = position + dir_neighbor
            # [search] if any neighbors give at least one free mouvement
            if (
                status_neighbor == current_status
                and self._get_status_on_walk_map(next_position) != current_status
            ):
                # [rec] recursive call on shape's neighbor
                result_is_taken &= self._recursive_is_taken(
                    next_position, current_status
                )
                # if current shape's neighbor has freedom (not taken) => we can exit (from the loop)
                if not result_is_taken:
                    # [optim] early exit
                    break

        # [end] return combine result
        return result_is_taken

    def is_taken(self, x, y):
        """
        Get the status of the stone

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            True if the stone is taken there and False otherwise
        """
        # init first recursive iteration
        current_status = self.get_status(x, y)
        # Is first position on empty case or out the board ?
        if current_status == Status.EMPTY or current_status == Status.OUT:
            return False
        # otherwise: current position is on stone
        # init walk-map (on Goban::is_taken scope)
        self._init_walk_map()
        # starting recursive search (on same stone) for an empty case
        return self._recursive_is_taken(Position(x, y), current_status)
