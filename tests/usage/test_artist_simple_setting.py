from loasim.calculate import DealCycle, calculate
from loasim.core import Enemy, InternalStat, Stat
from loasim.core.buff import BuffState, OnoffBuff
from loasim.job.artist import lostark_artist_skill_repository


def generate(internal_stat: InternalStat):
    SunDrawBuff = OnoffBuff(
        name="나만의 권능",
        stat=Stat(crit=49.7),
    )
    SunWellBuff = OnoffBuff(
        name="나만의 우물",
        stat=Stat(patt_indep=30),
    )

    OneStroke = lostark_artist_skill_repository.build(
        name="필법 : 한획긋기",
        level=11,
        gem=7,
        tripod={
            "거대한 붓": 5,
            "강화된 일격": 5,
        },
    )

    Cranes = lostark_artist_skill_repository.build(
        name="묵법 : 두루미나래",
        level=11,
        gem=5,
        tripod={
            "치명적인 일격": 5,
            "학익진": 5,
        },
    )

    Tiger = lostark_artist_skill_repository.build(
        name="묵법 : 범가르기",
        level=11,
        gem=6,
        tripod={
            "궤뚫는 일격": 5,
            "강화된 일격": 5,
        },
    )

    Moon = lostark_artist_skill_repository.build(
        name="묵법 : 달그리기",
        level=11,
        gem=7,
        tripod={
            "별 그리기": 4,
            "붉은 달": 4,
        },
    )

    InkRise = lostark_artist_skill_repository.build(
        name="묵법 : 먹오름",
        level=11,
        gem=5,
        tripod={
            "치명적인 일격": 1,
            "먹물점정": 1,
        },
    )

    state = {
        "나만의 권능": BuffState(onoff=True),
        "나만의 우물": BuffState(onoff=True),
    }

    return DealCycle(
        buff_list=[SunDrawBuff, SunWellBuff],
        skill_list=[
            (OneStroke, state, None),
            (Cranes, state, None),
            (Tiger, state, None),
            (Moon, state, None),
            (InkRise, state, None),
        ],
        cycle_time=12.127,
    )


calculate(
    internal_stat=InternalStat(
        weapon_att=28800, stat_main=119610, crit=537, special=56, swift=1691
    ),
    weapon_pdamage=21.86,
    setitem_state=[
        ("악몽", 2, 0),
        ("지배", 4, 0),
    ],
    engraving_state=[
        ("원한", 3),
        ("예리한 둔기", 3),
        ("안정된 상태", 3),
        ("돌격대장", 3),
        ("회귀", 3),
    ],
    card_state=["남겨진 바람의 절벽 (12)"],
    generator=generate,
    enemy=Enemy(armor=6000, reduction=23),
)
