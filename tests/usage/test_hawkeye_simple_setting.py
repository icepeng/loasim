from loguru import logger

from loasim.calculate import calculate
from loasim.card import lostark_default_card_repository
from loasim.core import Enemy, InternalStat, Stat
from loasim.Engraving import EngravingManager
from loasim.job import hawkeye
from loasim.setitem import SetItemState, lostark_setitem_repository

base_internal_stat = InternalStat(
    weapon_att=31392, stat_main=133748, crit=607, special=56, swift=1756
)
spd = base_internal_stat.get_spd() + 10  # 갈망 +10

base_stat = base_internal_stat.get_stat()
weapon_stat = Stat(pdamage=23.45)  # 무기 품질

logger.info(base_stat)
logger.info(weapon_stat)

setitem_state = [
    SetItemState(
        name="악몽",
        level_1=2,
        level_2=0,
    ),
    SetItemState(
        name="지배",
        level_1=4,
        level_2=0,
    ),
]

engraving_manager = EngravingManager(
    ("원한", 3), ("예리한 둔기", 3), ("타격의 대가", 3), ("아드레날린", 3), ("정밀 단도", 3)
)

card = lostark_default_card_repository.get("남겨진 바람의 절벽 (12)")
if card is None:
    raise

atomic_arrow_synergy = Stat(pdamage_indep=6)

basis_stat = (
    base_stat
    + weapon_stat
    + lostark_setitem_repository.get_stat(setitem_state)
    + engraving_manager.get_static_modifier()
    + card.stat
    + atomic_arrow_synergy
)

logger.info(basis_stat)

Snipe = hawkeye.Snipe.build_skill(
    gem=7,
    tripod={
        "약점 포착": 5,
        "손쉬운 먹잇감": 5,
    },
    additional_stat=basis_stat,
)

SharpShooter = hawkeye.SharpShooter.build_skill(
    gem=7,
    tripod={
        "급소 타격": 5,
        "약점 포착": 5,
        "집중 사격": 5,
    },
    additional_stat=basis_stat,
)

ChargingShot = hawkeye.ChargingShot.build_skill(
    gem=5,
    tripod={
        "더블 샷": 4,
        "즉발": 4,
    },
    additional_stat=basis_stat,
)

ArrowWave = hawkeye.ArrowWave.build_skill(
    gem=7,
    tripod={
        "강화된 화살": 4,
        "저속 탄환": 5,
        "웨이브 해일": 5,
    },
    additional_stat=basis_stat,
)

AtomicArrow = hawkeye.AtomicArrow.build_skill(
    gem=5,
    additional_stat=basis_stat,
)
AtomicArrowExplode = hawkeye.AtomicArrowExplode.build_skill(
    gem=5,
    additional_stat=basis_stat,
)
AtomicArrowElectric = hawkeye.AtomicArrowElectric.build_skill(
    gem=5,
    additional_stat=basis_stat,
)

ArrowShower = hawkeye.ArrowShower.build_skill(
    gem=5,
    tripod={
        "지속력 강화": 4,
        "장대비": 4,
    },
    additional_stat=basis_stat,
)

dealcycle = [  # 62s
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowShower, None),
    (ArrowWave, None),
    (SharpShooter, None),
    (Snipe, None),
    (ChargingShot, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowShower, None),
    (ArrowWave, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (SharpShooter, None),
    (Snipe, None),
    (ChargingShot, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowShower, None),
    (ArrowWave, None),
    (SharpShooter, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (Snipe, None),
    (ChargingShot, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowShower, None),
    (ArrowWave, None),
    (SharpShooter, None),
    (Snipe, None),
    (ChargingShot, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowShower, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowWave, None),
    (Snipe, None),
    (SharpShooter, None),
    (ChargingShot, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowShower, None),
    (ArrowWave, None),
    (Snipe, None),
    (SharpShooter, None),
    (ChargingShot, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (ArrowShower, None),
    (ArrowWave, None),
    (AtomicArrow, None),
    (AtomicArrowExplode, None),
    (AtomicArrowElectric, None),
    (Snipe, None),
    (SharpShooter, None),
    (ChargingShot, None),
]
cycle_time = 62

enemy = Enemy(armor=6000, reduction=23)

calculate(dealcycle, cycle_time, enemy)