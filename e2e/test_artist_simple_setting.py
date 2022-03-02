from loasim.calculate import DealCycle, calculate
from loasim.core import BuffState, Enemy, InternalStat
from loasim.job import SkillState


def calcuate_artist():
    state = {
        "저무는 달": BuffState(onoff=False),
        "내면의 각성": BuffState(onoff=True),
        "나만의 권능": BuffState(onoff=True),
        "나만의 우물": BuffState(onoff=True),
    }

    deal_cycle: DealCycle = [
        ("필법 : 한획긋기", state, None),
        ("묵법 : 두루미나래", state, None),
        ("묵법 : 범가르기", state, None),
        ("묵법 : 달그리기", state, None),
        ("묵법 : 먹오름", state, None),
    ]

    return calculate(
        job_name="artist",
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
        skill_state={
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
            "묵법 : 옹달샘": SkillState(
                level=11,
                gem=7,
                tripod={
                    "급소타격": 4,
                    "강화된 일격": 4,
                    "잉어 봉인해제!": 4,
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
        enemy=Enemy(armor=6000, reduction=23),
        deal_cycle=deal_cycle,
        cycle_time=12.127,
    )


def test_artist_simple_setting(snapshot: float):
    assert calcuate_artist() == snapshot


if __name__ == "__main__":
    calcuate_artist()
