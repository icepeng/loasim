import pytest

from loasim.core import Enemy, Skill, Stat


@pytest.mark.parametrize("att, expected_damage", [(1000, 11000), (0, 1000)])
def test_skill_damage(
    att: float,
    expected_damage: float,
    test_skill: Skill,
):
    assert (
        test_skill.get_damage(Enemy(armor=0, reduction=0), None, Stat(att=att))
        == expected_damage
    )
