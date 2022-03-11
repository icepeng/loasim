from os import path

from loasim.calculate import DealCycle, calculate
from loasim.character import Character
from loasim.core import Enemy
from loasim.util import load_config


def calculate_blade():
    character = Character.parse_obj(
        load_config(path.join(path.dirname(__file__), "configs", "blade_character.yml"))
    )
    deal_cycle = DealCycle.parse_obj(
        load_config(path.join(path.dirname(__file__), "configs", "blade_dealcycle.yml"))
    )

    return calculate(
        character=character,
        enemy=Enemy(armor=6000, reduction=23),
        deal_cycle=deal_cycle,
    )


def test_blade_simple_setting(snapshot: float):
    assert calculate_blade() == snapshot


if __name__ == "__main__":
    calculate_blade()
