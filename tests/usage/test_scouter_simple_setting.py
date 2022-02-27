from loasim.calculate import DealCycle, calculate
from loasim.core import Enemy, InternalStat, Stat, OnoffBuff
from loasim.core.buff import BuffState
from loasim.job.scouter import lostark_scouter_skill_repository


def generate(internal_stat: InternalStat):
    spd = internal_stat.get_spd()
    HyperSync = OnoffBuff(
        name="하이퍼 싱크",
        stat=Stat(patt_indep=6, pdamage_indep=internal_stat.special * 0.0886937),
    )

    RaidMissile = lostark_scouter_skill_repository.build(
        name="명령 : 레이드 미사일",
        level=12,
        gem=7,
        tripod={
            "오르간 미사일": 4,
            "약점 포착": 4,
        },
    )

    BabyDrone = lostark_scouter_skill_repository.build(
        name="명령 : 베이비 드론",
        level=12,
        gem=0,
        tripod={
            "급소 공격": 4,
            "일제 공격": 5,
        },
    )

    CometStrike = lostark_scouter_skill_repository.build(
        name="코멧 스트라이크",
        level=12,
        gem=9,
    )
    SlugShot = lostark_scouter_skill_repository.build(
        name="슬러그 샷",
        level=12,
        gem=9,
    )
    LaserBlade = lostark_scouter_skill_repository.build(
        name="레이저 블레이드",
        level=12,
        gem=9,
        additional_stat=Stat(pdamage_indep=20),  # Q-E 연계 20%
    )
    AccelionBeam = lostark_scouter_skill_repository.build(
        name="엑셀리온 빔",
        level=12,
        gem=9,
    )
    BurstBlow = lostark_scouter_skill_repository.build(
        name="버스트 블로우",
        level=12,
        gem=9,
    )
    CrimsonBreaker = lostark_scouter_skill_repository.build(
        name="크림슨 브레이커",
        level=12,
        gem=9,
    )

    sync_state = {
        "돌격대장": BuffState(onoff=True, stack=spd + 30),
        "진화의 유산": BuffState(onoff=True, stack=3),
        "하이퍼 싱크": BuffState(onoff=True),
    }
    nosync_state = {
        "돌격대장": BuffState(onoff=True, stack=spd),
        "진화의 유산": BuffState(onoff=False),
        "하이퍼 싱크": BuffState(onoff=False),
    }

    return DealCycle(
        buff_list=[HyperSync],
        skill_list=[  # 레미-베드-QESQRWAQEWQRWSQEWAQRW 23s
            (RaidMissile, nosync_state, None),
            (BabyDrone, nosync_state, None),
            (CometStrike, sync_state, None),
            (LaserBlade, sync_state, None),
            (CrimsonBreaker, sync_state, None),
            (CometStrike, sync_state, None),
            (AccelionBeam, sync_state, None),
            (SlugShot, sync_state, None),
            (BurstBlow, sync_state, None),
            (CometStrike, sync_state, None),
            (LaserBlade, sync_state, None),
            (SlugShot, sync_state, None),
            (CometStrike, sync_state, None),
            (AccelionBeam, sync_state, None),
            (SlugShot, sync_state, None),
            (CrimsonBreaker, sync_state, None),
            (CometStrike, sync_state, None),
            (LaserBlade, sync_state, None),
            (SlugShot, sync_state, None),
            (BurstBlow, sync_state, None),
            (CometStrike, sync_state, None),
            (AccelionBeam, sync_state, None),
            (SlugShot, sync_state, None),
        ],
        cycle_time=23
    )


calculate(
    internal_stat=InternalStat(
        weapon_att=50362, stat_main=156350, crit=632, special=1776, swift=53
    ),
    weapon_pdamage=23.45,
    card_state=["남겨진 바람의 절벽 (12)"],
    setitem_state=[
        ("환각", 6, 6)
    ],
    engraving_state=[
        ("원한", 3),
        ("예리한 둔기", 3),
        ("바리케이드", 3),
        ("돌격대장", 3),
        ("아드레날린", 3),
        ("진화의 유산", 1),
    ],
    generator=generate,
    enemy=Enemy(armor=6000, reduction=23),
)
