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

    MoonlightSonic = lostark_blade_skill_repository.build(
        name="문라이트 소닉",
        level=11,
        gem=7,
        tripod={
            "암흑 공격": 5,
            "지속력 강화": 4,
            "쉐이드 소닉": 4,
        },
    )

    BladeBurst = lostark_blade_skill_repository.build(
        name="블레이드 버스트",
        level=11,
        gem=7,
        additional_stat=Stat(pdamage_indep=internal_stat.special * 0.11444),
    )

    blade_arts_state = {
        "블레이드 아츠": True,
        "약점 노출": True,
        "잔재된 기운": 0,
    }
    no_blade_arts_state = {
        "블레이드 아츠": False,
        "약점 노출": True,
        "잔재된 기운": 3,
    }

    return DealCycle(
        buff_list=[SpinCutterBuff, BladeArts3],
        skill_list=[
            (SpinCutter, no_blade_arts_state, "back"),
            (SpinCutter, no_blade_arts_state, "back"),
            (SpinCutter, no_blade_arts_state, "back"),
            (SoulAbsorber, no_blade_arts_state, "back"),
            (VoidStrike, no_blade_arts_state, "back"),
            (BlitzRush, no_blade_arts_state, "back"),
            (BladeBurst, blade_arts_state, "back"),
            (MoonlightSonic, no_blade_arts_state, "back"),
        ],
        cycle_time=10,
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
        ("아드레날린", 3),
        ("잔재된 기운", 3),
    ],
    card_state=["남겨진 바람의 절벽 (12)"],
    generator=generate,
    enemy=Enemy(armor=6000, reduction=23),
)
