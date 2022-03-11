import pytest

from loasim.core import InternalStat
from loasim.job import SkillState, get_job


@pytest.fixture
def test_destroyer():
    return get_job("destroyer").build(
        {
            "헤비 크러쉬": SkillState(
                level=12,
                gem=0,
                tripod={},
            ),
            "인듀어 페인": SkillState(
                level=10,
                gem=0,
                tripod={
                    "고통의 흔적": 1,
                },
            ),
            "그라비티 임팩트": SkillState(level=10, gem=0, tripod={}),
            "드레드노트": SkillState(
                level=11,
                gem=0,
                tripod={
                    "몰아치는 해머": 5,
                },
            ),
            "러닝 크래쉬": SkillState(
                level=7,
                gem=0,
                tripod={},
            ),
            "퍼펙트 스윙": SkillState(
                level=12,
                gem=9,
                tripod={
                    "약점포착": 5,
                    "날카로운 해머": 5,
                    "무절제": 5,
                },
            ),
            "사이즈믹 해머": SkillState(
                level=12,
                gem=9,
                tripod={
                    "절대적인 힘": 5,
                    "날카로운 벽": 5,
                    "굶주린 힘": 5,
                },
            ),
            "풀 스윙": SkillState(
                level=12,
                gem=9,
                tripod={
                    "빠른 준비": 5,
                    "무서운 해머": 5,
                    "야수의 눈": 5,
                },
            ),
        },
        InternalStat(
            weapon_att=52051, stat_main=198850, crit=1471, special=449, swift=544
        ),
    )
