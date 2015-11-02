from random import randint

import pytest

from onagame2015.lib import Coordinate
from onagame2015.units import AttackUnit
from onagame2015.arena import ArenaGrid, TileContainer

VALID_MOVES = (Coordinate(1, 0), Coordinate(-1, 0),
               Coordinate(0, 1), Coordinate(0, -1),
                )


INVALID_MOVES_FROM_00 = (Coordinate(-1, 0), Coordinate(0, -1))

INVALID_INPUTS = ('UP', 2334, 0.343)


@pytest.mark.parametrize('invalid_input', INVALID_INPUTS)
def test_attack_unit_move_invalid_input(random_arena, invalid_input):
    initial_coordinate = Coordinate(0, 0)
    attack_unit = AttackUnit(initial_coordinate, 1, random_arena)

    result = attack_unit.move(invalid_input)

    assert result.get('error') and 'invalid' in result.get('error')
    assert attack_unit.coordinate == initial_coordinate


@pytest.mark.parametrize('invalid_move', INVALID_MOVES_FROM_00 + (999999, 123))
def test_attack_unit_move_out_of_arena(random_arena, invalid_move):
    initial_coordinate = Coordinate(0, 0)
    attack_unit = AttackUnit(initial_coordinate, 1, random_arena)

    result = attack_unit.move((99999, 99999))

    assert result.get('error') and 'invalid' in result.get('error')
    assert attack_unit.coordinate == initial_coordinate


@pytest.mark.parametrize('valid_move', VALID_MOVES)
def test_attack_unit_move(random_arena, valid_move):
    initial_coordinate = Coordinate(1, 1)
    attack_unit = AttackUnit(initial_coordinate, 1, random_arena)

    result = attack_unit.move(valid_move)

    assert not result.get('error')
