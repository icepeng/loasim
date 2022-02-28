from loasim.calculate import DealCycle, calculate
from loasim.core import Enemy, InternalStat
from loasim.core.buff import BuffState
from loasim.job import SkillState

state = {
    "피해 증폭": BuffState(onoff=True),
}

deal_cycle: DealCycle = [
    ("아토믹 애로우", state, None),
    ("애로우 샤워", state, None),
    ("애로우 해일", state, None),
    ("샤프 슈터", state, None),
    ("스나이프", state, None),
    ("차징 샷", state, None),
    ("아토믹 애로우", state, None),
    ("애로우 샤워", state, None),
    ("애로우 해일", state, None),
    ("아토믹 애로우", state, None),
    ("샤프 슈터", state, None),
    ("스나이프", state, None),
    ("차징 샷", state, None),
    ("아토믹 애로우", state, None),
    ("애로우 샤워", state, None),
    ("애로우 해일", state, None),
    ("샤프 슈터", state, None),
    ("아토믹 애로우", state, None),
    ("스나이프", state, None),
    ("차징 샷", state, None),
    ("아토믹 애로우", state, None),
    ("애로우 샤워", state, None),
    ("애로우 해일", state, None),
    ("샤프 슈터", state, None),
    ("스나이프", state, None),
    ("차징 샷", state, None),
    ("아토믹 애로우", state, None),
    ("애로우 샤워", state, None),
    ("아토믹 애로우", state, None),
    ("애로우 해일", state, None),
    ("스나이프", state, None),
    ("샤프 슈터", state, None),
    ("차징 샷", state, None),
    ("아토믹 애로우", state, None),
    ("애로우 샤워", state, None),
    ("애로우 해일", state, None),
    ("스나이프", state, None),
    ("샤프 슈터", state, None),
    ("차징 샷", state, None),
    ("아토믹 애로우", state, None),
    ("애로우 샤워", state, None),
    ("애로우 해일", state, None),
    ("아토믹 애로우", state, None),
    ("스나이프", state, None),
    ("샤프 슈터", state, None),
    ("차징 샷", state, None),
]

calculate(
    job_name="hawkeye",
    internal_stat=InternalStat(
        weapon_att=31392, stat_main=133748, crit=607, special=56, swift=1756
    ),
    weapon_pdamage=23.45,
    setitem_state=[
        ("악몽", 2, 0),
        ("지배", 4, 0),
    ],
    engraving_state=[
        ("원한", 3),
        ("예리한 둔기", 3),
        ("타격의 대가", 3),
        ("아드레날린", 3),
        ("정밀 단도", 3),
    ],
    card_state=["남겨진 바람의 절벽 (12)"],
    skill_state={
        "스나이프": SkillState(
            level=12,
            gem=7,
            tripod={
                "약점 포착": 5,
                "손쉬운 먹잇감": 5,
            },
        ),
        "샤프 슈터": SkillState(
            level=12,
            gem=7,
            tripod={
                "급소 타격": 5,
                "약점 포착": 5,
                "집중 사격": 5,
            },
        ),
        "차징 샷": SkillState(
            level=12,
            gem=5,
            tripod={
                "더블 샷": 4,
                "즉발": 4,
            },
        ),
        "애로우 해일": SkillState(
            level=12,
            gem=7,
            tripod={
                "강화된 화살": 4,
                "저속 탄환": 5,
                "웨이브 해일": 5,
            },
        ),
        "아토믹 애로우": SkillState(
            level=12,
            gem=5,
            tripod={
                "피해 증폭": 1,
                "전격 화살": 4,
            },
        ),
        "애로우 샤워": SkillState(
            level=10,
            gem=5,
            tripod={
                "지속력 강화": 4,
                "장대비": 4,
            },
        ),
    },
    enemy=Enemy(armor=6000, reduction=23),
    deal_cycle=deal_cycle,
    cycle_time=62,
)
