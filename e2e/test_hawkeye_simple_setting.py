from os import path

from loasim.calculate import DealCycle, calculate
from loasim.character import Character
from loasim.core import Enemy
from loasim.util import load_config


def calculate_hawkeye():
    character = Character.parse_obj(
        load_config(
            path.join(path.dirname(__file__), "configs", "hawkeye_character.yml")
        )
    )
    deal_cycle = DealCycle.parse_obj(
        load_config(
            path.join(path.dirname(__file__), "configs", "hawkeye_dealcycle.yml")
        )
    )

    return calculate(
        character=character,
        enemy=Enemy(armor=6000, reduction=23),
        deal_cycle=deal_cycle,
    )


def test_hawkeye_simple_setting(snapshot: float):
    assert calculate_hawkeye() == snapshot


if __name__ == "__main__":
    calculate_hawkeye()
