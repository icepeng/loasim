from loasim.calculate import DealCycle, calculate
from loasim.core import Enemy, InternalStat, Stat
from loasim.core.buff import OnoffBuff
from loasim.job.hawkeye import lostark_hawkeye_skill_repository


def generate(internal_stat: InternalStat):
    AtomicArrowSynergy = OnoffBuff(name="피해 증폭", stat=Stat(pdamage_indep=6))

    Snipe = lostark_hawkeye_skill_repository.build(
        name="스나이프",
        level=12,
        gem=7,
        tripod={
            "약점 포착": 5,
            "손쉬운 먹잇감": 5,
        },
    )

    SharpShooter = lostark_hawkeye_skill_repository.build(
        name="샤프 슈터",
        level=12,
        gem=7,
        tripod={
            "급소 타격": 5,
            "약점 포착": 5,
            "집중 사격": 5,
        },
    )

    ChargingShot = lostark_hawkeye_skill_repository.build(
        name="차징 샷",
        level=12,
        gem=5,
        tripod={
            "더블 샷": 4,
            "즉발": 4,
        },
    )

    ArrowWave = lostark_hawkeye_skill_repository.build(
        name="애로우 해일",
        level=12,
        gem=7,
        tripod={
            "강화된 화살": 4,
            "저속 탄환": 5,
            "웨이브 해일": 5,
        },
    )

    AtomicArrow = lostark_hawkeye_skill_repository.build(
        name="아토믹 애로우",
        level=12,
        gem=5,
    )

    ArrowShower = lostark_hawkeye_skill_repository.build(
        name="애로우 샤워",
        level=10,
        gem=5,
        tripod={
            "지속력 강화": 4,
            "장대비": 4,
        },
    )

    state = {
        "피해 증폭": True,
    }

    return DealCycle(
        buff_list=[AtomicArrowSynergy],
        skill_list=[
            (AtomicArrow, state, None),
            (ArrowShower, state, None),
            (ArrowWave, state, None),
            (SharpShooter, state, None),
            (Snipe, state, None),
            (ChargingShot, state, None),
            (AtomicArrow, state, None),
            (ArrowShower, state, None),
            (ArrowWave, state, None),
            (AtomicArrow, state, None),
            (SharpShooter, state, None),
            (Snipe, state, None),
            (ChargingShot, state, None),
            (AtomicArrow, state, None),
            (ArrowShower, state, None),
            (ArrowWave, state, None),
            (SharpShooter, state, None),
            (AtomicArrow, state, None),
            (Snipe, state, None),
            (ChargingShot, state, None),
            (AtomicArrow, state, None),
            (ArrowShower, state, None),
            (ArrowWave, state, None),
            (SharpShooter, state, None),
            (Snipe, state, None),
            (ChargingShot, state, None),
            (AtomicArrow, state, None),
            (ArrowShower, state, None),
            (AtomicArrow, state, None),
            (ArrowWave, state, None),
            (Snipe, state, None),
            (SharpShooter, state, None),
            (ChargingShot, state, None),
            (AtomicArrow, state, None),
            (ArrowShower, state, None),
            (ArrowWave, state, None),
            (Snipe, state, None),
            (SharpShooter, state, None),
            (ChargingShot, state, None),
            (AtomicArrow, state, None),
            (ArrowShower, state, None),
            (ArrowWave, state, None),
            (AtomicArrow, state, None),
            (Snipe, state, None),
            (SharpShooter, state, None),
            (ChargingShot, state, None),
        ],
        cycle_time=62,
    )


calculate(
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
    generator=generate,
    enemy=Enemy(armor=6000, reduction=23),
)
