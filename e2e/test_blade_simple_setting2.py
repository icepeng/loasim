from loasim.calculate import DealCycle, calculate
from loasim.core import BuffState, Enemy, InternalStat
from loasim.job import SkillState


def calculate_blade():
    burst_state = {
        "약점 노출": BuffState(onoff=True),
        "블레이드 아츠": BuffState(onoff=True),
        "버스트": BuffState(onoff=True, stack=12),
    }
    blade_arts_state = {
        "약점 노출": BuffState(onoff=True),
        "블레이드 아츠": BuffState(onoff=True),
        "버스트": BuffState(onoff=False),
    }
    no_blade_arts_state = {
        "약점 노출": BuffState(onoff=True),
        "블레이드 아츠": BuffState(onoff=False),
        "버스트": BuffState(onoff=False),
    }

    deal_cycle: DealCycle = [
        ("스핀 커터", blade_arts_state, "back"),
        ("스핀 커터", blade_arts_state, "back"),
        ("스핀 커터", blade_arts_state, "back"),
        ("윈드 컷", blade_arts_state, "back"),
        ("소울 앱소버", blade_arts_state, "back"),
        ("어스 슬래쉬", blade_arts_state, "back"),
        ("블리츠 러시", blade_arts_state, "back"),
        ("윈드 컷", blade_arts_state, "back"),
        ("블레이드 버스트", burst_state, "back"),
        ("보이드 스트라이크", no_blade_arts_state, "back"),
    ]

    return calculate(
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
            ("예리한 둔기", 3),
            ("버스트", 3),
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
            "윈드 컷": SkillState(
                level=11,
                gem=5,
                tripod={
                    "지속력 강화": 4,
                },
            ),
            "어스 슬래쉬": SkillState(
                level=10,
                gem=5,
                tripod={
                    "밀어내기": 4,
                    "약점 포착": 4,
                    "대지 폭발": 4,
                },
            ),
            "블레이드 버스트": SkillState(
                level=11,
                gem=7,
            ),
        },
        enemy=Enemy(armor=6000, reduction=23),
        deal_cycle=deal_cycle,
        cycle_time=9.375,
    )


def test_blade_simple_setting2(snapshot: float):
    assert calculate_blade() == snapshot


if __name__ == "__main__":
    calculate_blade()
