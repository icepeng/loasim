import pytest
from loasim.core.skill import Tripod, Skill, SkillSpecification, SkillBuildConfiguration
from loasim.core.stat import Stat


@pytest.fixture
def test_skill_specification():
    return SkillSpecification(
        name="명령 : 레이드 미사일",
        base=3066,
        coefficient=19.10,
        tripods=[
            Tripod(
                name="오르간 미사일",
                stat_list=[
                    Stat(pdamage_indep=-30)
                    + Stat(pdamage_indep=100),
                    Stat(pdamage_indep=-27)
                    + Stat(pdamage_indep=100),
                    Stat(pdamage_indep=-23)
                    + Stat(pdamage_indep=100),
                    Stat(pdamage_indep=-19)
                    + Stat(pdamage_indep=100),
                    Stat(pdamage_indep=-15)
                    + Stat(pdamage_indep=100),
                ],
            ),
            Tripod(
                name="약점 포착",
                stat_list=[
                    Stat(pdamage_indep=60),
                    Stat(pdamage_indep=69),
                    Stat(pdamage_indep=78),
                    Stat(pdamage_indep=87),
                    Stat(pdamage_indep=96),
                ],
            ),
        ],
    )