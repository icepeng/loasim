from loguru import logger

from loasim.calculate import DealCycle, calculate
from loasim.core import Enemy, InternalStat, Stat
from loasim.core.buff import OnoffBuff
from loasim.core.stat import sub_pdamage_indep
from loasim.job.blade import lostark_blade_skill_repository


def generate(internal_stat: InternalStat):
    SpinCutterBuff = OnoffBuff(
        name="약점 노출",
        stat=Stat(pdamage_indep=3, pdamage_indep_back=sub_pdamage_indep(12, 3)),
    )
    BladeArts3 = OnoffBuff(
        name="블레이드 아츠",
        stat=Stat(patt_job=30),
    )

    SpinCutter = lostark_blade_skill_repository.build(
        name="스핀 커터",
        level=10,
    )

    SoulAbsorber = lostark_blade_skill_repository.build(
        name="소울 앱소버",
        level=11,
        gem=7,
        tripod={
            "암흑 공격": 5,
            "반 가르기": 4,
        },
    )

    VoidStrike = lostark_blade_skill_repository.build(
        name="보이드 스트라이크",
        level=11,
        gem=7,
        tripod={
            "암흑 공격": 4,
            "블랙 익스플로젼": 4,
        },
    )

    BlitzRush = lostark_blade_skill_repository.build(
        name="블리츠 러시",
        level=11,
        gem=7,
        tripod={
            "급소 타격": 4,
            "차지 강화": 5,
            "쉐도우 러시": 5,
        },
    )

    WindCut = lostark_blade_skill_repository.build(
        name="윈드 컷",
        level=11,
        gem=5,
        tripod={
            "지속력 강화": 4,
        },
    )

    EarthSlash = lostark_blade_skill_repository.build(
        name="어스 슬래쉬",
        level=10,
        gem=5,
        tripod={
            "밀어내기": 4,
            "약점 포착": 4,
            "대지 폭발": 4,
        },
    )

    BladeBurst = lostark_blade_skill_repository.build(
        name="블레이드 버스트",
        level=11,
        gem=7,
        additional_stat=Stat(pdamage_indep=internal_stat.special * 0.11444),
    )

    burst_state = {
        "약점 노출": True,
        "블레이드 아츠": True,
        "버스트": 12,
    }
    blade_arts_state = {
        "약점 노출": True,
        "블레이드 아츠": True,
        "버스트": 0,
    }
    no_blade_arts_state = {
        "약점 노출": True,
        "블레이드 아츠": False,
        "버스트": 0,
    }

    return DealCycle(
        buff_list=[SpinCutterBuff, BladeArts3],
        skill_list=[
            (SpinCutter, blade_arts_state, "back"),
            (SpinCutter, blade_arts_state, "back"),
            (SpinCutter, blade_arts_state, "back"),
            (WindCut, blade_arts_state, "back"),
            (SoulAbsorber, blade_arts_state, "back"),
            (EarthSlash, blade_arts_state, "back"),
            (BlitzRush, blade_arts_state, "back"),
            (WindCut, blade_arts_state, "back"),
            (BladeBurst, burst_state, "back"),
            (VoidStrike, no_blade_arts_state, "back"),
        ],
        cycle_time=9.375,
    )


calculate(
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
    generator=generate,
    enemy=Enemy(armor=6000, reduction=23),
)
