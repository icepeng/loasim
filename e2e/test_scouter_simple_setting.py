from loasim.calculate import DealCycle, calculate
from loasim.core import Enemy, InternalStat, Stat
from loasim.core.buff import BuffState
from loasim.job.base import SkillState

sync0_state = {
    "환각": BuffState(onoff=False),
    "실체": BuffState(onoff=True),
    "진화의 유산": BuffState(onoff=True, stack=0),
    "하이퍼 싱크": BuffState(onoff=True),
}
sync1_state = {
    "환각": BuffState(onoff=False),
    "실체": BuffState(onoff=True),
    "진화의 유산": BuffState(onoff=True, stack=1),
    "하이퍼 싱크": BuffState(onoff=True),
}
sync2_state = {
    "환각": BuffState(onoff=False),
    "실체": BuffState(onoff=True),
    "진화의 유산": BuffState(onoff=True, stack=2),
    "하이퍼 싱크": BuffState(onoff=True),
}
sync3_state = {
    "환각": BuffState(onoff=False),
    "실체": BuffState(onoff=True),
    "진화의 유산": BuffState(onoff=True, stack=3),
    "하이퍼 싱크": BuffState(onoff=True),
}
nosync_state = {
    "환각": BuffState(onoff=False),
    "실체": BuffState(onoff=True),
    "진화의 유산": BuffState(onoff=False),
    "하이퍼 싱크": BuffState(onoff=False),
}

deal_cycle: DealCycle = [  # 레미-베드-QESQRWAQEWQRWSQEWAQRW 23s
    ("명령 : 레이드 미사일", nosync_state, None),
    ("명령 : 베이비 드론", nosync_state, None),
    ("코멧 스트라이크", sync0_state, None),
    ("레이저 블레이드", sync1_state, None),
    ("크림슨 브레이커", sync2_state, None),
    ("코멧 스트라이크", sync3_state, None),
    ("엑셀리온 빔", sync3_state, None),
    ("슬러그 샷", sync3_state, None),
    ("버스트 블로우", sync3_state, None),
    ("코멧 스트라이크", sync3_state, None),
    ("레이저 블레이드", sync3_state, None),
    ("슬러그 샷", sync3_state, None),
    ("코멧 스트라이크", sync3_state, None),
    ("엑셀리온 빔", sync3_state, None),
    ("슬러그 샷", sync3_state, None),
    ("크림슨 브레이커", sync3_state, None),
    ("코멧 스트라이크", sync3_state, None),
    ("레이저 블레이드", sync3_state, None),
    ("슬러그 샷", sync3_state, None),
    ("버스트 블로우", sync3_state, None),
    ("코멧 스트라이크", sync3_state, None),
    ("엑셀리온 빔", sync3_state, None),
    ("슬러그 샷", sync3_state, None),
]

calculate(
    job_name="scouter",
    internal_stat=InternalStat(
        weapon_att=50362, stat_main=156350, crit=632, special=1776, swift=53
    ),
    weapon_pdamage=23.45,
    card_state=["남겨진 바람의 절벽 (12)"],
    setitem_state=[("환각", 6, 6)],
    engraving_state=[
        ("원한", 3),
        ("예리한 둔기", 3),
        ("바리케이드", 3),
        ("돌격대장", 3),
        ("아드레날린", 3),
        ("진화의 유산", 1),
    ],
    skill_state={
        "명령 : 레이드 미사일": SkillState(
            level=12,
            gem=7,
            tripod={
                "오르간 미사일": 4,
                "약점 포착": 4,
            },
        ),
        "명령 : 베이비 드론": SkillState(
            level=12,
            gem=0,
            tripod={
                "급소 공격": 4,
                "일제 공격": 5,
            },
        ),
        "코멧 스트라이크": SkillState(
            level=12,
            gem=9,
        ),
        "슬러그 샷": SkillState(
            level=12,
            gem=9,
        ),
        "레이저 블레이드": SkillState(
            level=12,
            gem=9,
            additional_stat=Stat(pdamage_indep=20),  # Q-E 연계 20%
        ),
        "엑셀리온 빔": SkillState(
            level=12,
            gem=9,
        ),
        "버스트 블로우": SkillState(
            level=12,
            gem=9,
        ),
        "크림슨 브레이커": SkillState(
            level=12,
            gem=9,
        ),
    },
    enemy=Enemy(armor=6000, reduction=23),
    deal_cycle=deal_cycle,
    cycle_time=23,
)
