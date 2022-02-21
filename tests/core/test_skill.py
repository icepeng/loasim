from loasim.core.skill import Skill, SkillSpecification
import pytest

from loasim.core.enemy import Enemy

@pytest.mark.parametrize('skill_gem, skill_tripod', [
    (7, {"오르간 미사일": 4}),
    (9, {"오르간 미사일": 4, "약점 포착": 4}),
])
def test_skill_build(skill_gem, skill_tripod, test_skill_specification):
    skill = test_skill_specification.build_skill(
        gem=skill_gem,
        tripod=skill_tripod
    )

    skill.get_damage(Enemy(armor=6000, reduction=23))
