from loasim.calculate import DealCycle, calculate
from loasim.core import BuffState, Enemy, InternalStat
from loasim.core.stat import Stat
from loasim.job import SkillState


def calculate_destroyer():
    core_indure_state = {
        "고통의 흔적": BuffState(onoff=True),
        "분노의 망치": BuffState(onoff=False),
        "중력 코어": BuffState(onoff=False),
    }
    core_no_indure_state = {
        "고통의 흔적": BuffState(onoff=False),
        "분노의 망치": BuffState(onoff=False),
        "중력 코어": BuffState(onoff=False),
    }
    release_indure_state = {
        "고통의 흔적": BuffState(onoff=True),
        "분노의 망치": BuffState(onoff=True),
        "중력 코어": BuffState(onoff=True, stack=3),
    }
    release_no_indure_state = {
        "고통의 흔적": BuffState(onoff=False),
        "분노의 망치": BuffState(onoff=True),
        "중력 코어": BuffState(onoff=True, stack=3),
    }

    deal_cycle: DealCycle = [
        ("사이즈믹 해머", release_indure_state, "head"),
        ("인듀어 페인", core_no_indure_state, "head"),
        ("그라비티 임팩트", core_indure_state, "head"),
        ("풀 스윙", release_indure_state, "head"),
        ("헤비 크러쉬", core_indure_state, "head"),
        ("러닝 크래쉬", core_no_indure_state, "head"),
        ("퍼펙트 스윙", release_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("그라비티 임팩트", core_no_indure_state, "head"),
        ("풀 스윙", release_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("드레드노트", core_no_indure_state, "head"),
        ("사이즈믹 해머", release_no_indure_state, "head"),
        ("그라비티 임팩트", core_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("풀 스윙", release_no_indure_state, "head"),
        ("러닝 크래쉬", core_no_indure_state, "head"),
        ("인듀어 페인", core_no_indure_state, "head"),
        ("퍼펙트 스윙", release_indure_state, "head"),
        ("헤비 크러쉬", core_indure_state, "head"),
        ("그라비티 임팩트", core_no_indure_state, "head"),
        ("풀 스윙", release_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("드레드노트", core_no_indure_state, "head"),
        ("사이즈믹 해머", release_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("그라비티 임팩트", core_no_indure_state, "head"),
        ("풀 스윙", release_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("러닝 크래쉬", core_no_indure_state, "head"),
        ("퍼펙트 스윙", release_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("그라비티 임팩트", core_no_indure_state, "head"),
        ("풀 스윙", release_no_indure_state, "head"),
        ("헤비 크러쉬", core_no_indure_state, "head"),
        ("드레드노트", core_no_indure_state, "head"),
    ]

    return calculate(
        job_name="destroyer",
        internal_stat=InternalStat(
            weapon_att=52051, stat_main=198850, crit=1471, special=449, swift=544
        ),
        weapon_pdamage=28.44,
        setitem_state=[("사멸", 6, 6)],
        engraving_state=[
            ("원한", 3),
            ("슈퍼 차지", 3),
            ("분노의 망치", 3),
            ("바리케이드", 3),
            ("저주받은 인형", 3),
        ],
        card_state=["세상을 구하는 빛 (18)"],
        skill_state={
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
        enemy=Enemy(armor=6000, reduction=23),
        deal_cycle=deal_cycle,
        cycle_time=68,
        additional_stat=Stat(
            pdamage_indep=3 / 3, crit=5 / 3, crit_damage=8 / 3
        ),  # 순환 팔찌
    )


def test_destroyer_simple_setting(snapshot: float):
    assert calculate_destroyer() == snapshot


if __name__ == "__main__":
    calculate_destroyer()
