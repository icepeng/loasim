import os
from typing import Any, Dict

import yaml

from loasim.calculate import DealCycle, calculate
from loasim.character import Character
from loasim.core import BuffState, Enemy, InternalStat
from loasim.job import SkillState


def save(filename: str, obj: Dict[str, Any]):
    with open(
        os.path.join(os.path.dirname(__file__), filename),
        mode="w",
        encoding="utf8",
    ) as f:
        yaml.safe_dump(obj, f, allow_unicode=True, sort_keys=False)


def load(filename: str):
    with open(
        os.path.join(os.path.dirname(__file__), filename),
        encoding="utf8",
    ) as f:
        return yaml.safe_load(f)


character = Character(
    job_name="blade",
    internal_stat=InternalStat(
        weapon_att=41814, stat_main=137148, crit=568, special=1733, swift=28
    ),
    weapon_pdamage=30,
    setitem_state=[
        ("사멸", 6, 4),
    ],
    engraving_state=[
        ("원한", 3),
        ("슈퍼 차지", 3),
        ("기습의 대가", 3),
        ("아드레날린", 3),
        ("잔재된 기운", 3),
    ],
    card_state=["남겨진 바람의 절벽 (12)"],
    skill_state={
        "스핀 커터": SkillState(
            level=10,
            tripod={
                "약점 노출": 1,
            },
        ),
        "소울 앱소버": SkillState(
            level=11,
            gem=7,
            tripod={
                "암흑 공격": 5,
                "반 가르기": 4,
            },
        ),
        "보이드 스트라이크": SkillState(
            level=11,
            gem=7,
            tripod={
                "암흑 공격": 4,
                "블랙 익스플로젼": 4,
            },
        ),
        "블리츠 러시": SkillState(
            level=11,
            gem=7,
            tripod={
                "급소 타격": 4,
                "차지 강화": 5,
                "쉐도우 러시": 5,
            },
        ),
        "문라이트 소닉": SkillState(
            level=11,
            gem=7,
            tripod={
                "암흑 공격": 5,
                "지속력 강화": 4,
                "쉐이드 소닉": 4,
            },
        ),
        "블레이드 버스트": SkillState(
            level=11,
            gem=7,
        ),
    },
)
