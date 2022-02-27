from typing import Dict
import pytest

from loasim.core.enemy import Enemy
from loasim.core.skill import SkillSpecification, SkillRepository


@pytest.mark.parametrize(
    "skill_gem, skill_tripod",
    [
        (7, {"오르간 미사일": 4}),
        (9, {"오르간 미사일": 4, "약점 포착": 4}),
    ],
)
def test_skill_build(
    skill_gem: int,
    skill_tripod: Dict[str, int],
    test_skill_specification: SkillSpecification,
):
    skill_repository = SkillRepository()
    skill_repository.add(test_skill_specification)
    skill = skill_repository.build(
        name=test_skill_specification.name, level=12, gem=skill_gem, tripod=skill_tripod
    )

    skill.get_damage(Enemy(armor=6000, reduction=23))
