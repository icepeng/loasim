from loasim.core import InternalStat
from loasim.job import SkillState, get_job


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
