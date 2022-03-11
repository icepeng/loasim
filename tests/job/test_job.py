from typing import Dict, List, Tuple

import pytest

from loasim.core import AbstractBuff, BuffState, InternalStat, Skill, Stat
from loasim.job import Job, SkillSpecification, SkillState, get_job

eps = 1e-8


@pytest.mark.parametrize(
    "level, base, coefficient",
    [
        (10, 100, 10),
        (11, 110, 11),
        (12, 120, 12),
    ],
)
def test_job_build_skill(level: int, base: float, coefficient: float):
    test_job = Job()
    test_job.add_skill(
        SkillSpecification(
            name="테스트 스킬",
            damage_table={
                10: (100, 10),
                11: (110, 11),
                12: (120, 12),
            },
            type="Normal",
        )
    )

    skills, _ = test_job.build(
        {
            "테스트 스킬": SkillState(level=level),
        },
        InternalStat(),
    )

    assert skills["테스트 스킬"].base == base
    assert skills["테스트 스킬"].coefficient == coefficient


def test_job_artist():
    get_job("artist").build(
        {
            "묵법 : 해그리기": SkillState(
                level=10,
                tripod={
                    "나만의 권능": 5,
                },
            ),
            "묵법 : 해우물": SkillState(
                level=10,
                tripod={
                    "나만의 우물": 1,
                },
            ),
            "필법 : 한획긋기": SkillState(
                level=11,
                gem=7,
                tripod={
                    "거대한 붓": 5,
                    "강화된 일격": 5,
                },
            ),
            "묵법 : 두루미나래": SkillState(
                level=11,
                gem=5,
                tripod={
                    "치명적인 일격": 5,
                    "학익진": 5,
                },
            ),
            "묵법 : 범가르기": SkillState(
                level=11,
                gem=6,
                tripod={
                    "궤뚫는 일격": 5,
                    "강화된 일격": 5,
                },
            ),
            "묵법 : 달그리기": SkillState(
                level=11,
                gem=7,
                tripod={
                    "별 그리기": 4,
                    "붉은 달": 4,
                },
            ),
            "묵법 : 먹오름": SkillState(
                level=11,
                gem=5,
                tripod={
                    "치명적인 일격": 1,
                    "먹물점정": 1,
                },
            ),
        },
        InternalStat(
            weapon_att=28800, stat_main=119610, crit=537, special=56, swift=1691
        ),
    )


@pytest.mark.parametrize(
    "core_stack, special, expected_pdamage_indep",
    [
        (0, 0, 0),
        (1, 0, 10),
        (2, 0, 20),
        (3, 0, 45),
        (0, 1000, 0),
        (1, 1000, 10 * 1.82255),
        (2, 1000, 20 * 1.82255),
        (3, 1000, 45 * 1.82255),
    ],
)
def test_job_destroyer(
    core_stack: int,
    special: float,
    expected_pdamage_indep: float,
    test_destroyer: Tuple[Dict[str, Skill], List[AbstractBuff]],
):
    skills, buffs = test_destroyer

    gravity_core_buff = next(buff for buff in buffs if buff.name == "중력 코어")
    gravity_core_stat = gravity_core_buff.get_stat(
        {"중력 코어": BuffState(onoff=True, stack=core_stack)},
        skills["사이즈믹 해머"],
        stat=Stat(),
        internal_stat=InternalStat(special=special),
    )

    assert abs(gravity_core_stat.pdamage_indep - expected_pdamage_indep) < eps
