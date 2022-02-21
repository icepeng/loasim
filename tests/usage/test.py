from loasim.calculate import calculate
from loguru import logger

from loasim.core import Stat, InternalStat, Enemy

from loasim.setitem import lostark_setitem_repository, SetItemState
from loasim.card import lostark_default_card_repository

from loasim.engraving import EngravingManager
from loasim.job import scouter


base_internal_stat = InternalStat(weapon_att=50362, stat_main=156350, crit=632, special=1776, swift=53)
spd = base_internal_stat.get_spd() + 10  # 갈망 +10

base_stat = base_internal_stat.get_stat()
weapon_stat = Stat(pdamage=23.45)  # 무기 품질

logger.info(base_stat)
logger.info(weapon_stat)

setitem_state = [SetItemState(
    name='환각',
    level_1=6,
    level_2=6,
)]

engraving_manager = EngravingManager(
    ("원한", 3), ("예리한 둔기", 3), ("바리케이드", 3), ("돌격대장", 3), ("아드레날린", 3), ("진화의 유산", 1)
)

basis_stat = (
    base_stat
    + weapon_stat
    + lostark_setitem_repository.get_stat(setitem_state)
    + engraving_manager.get_static_modifier()
    + lostark_default_card_repository.get("남겨진 바람의 절벽 (12)").stat
)

logger.info(basis_stat)
HyperSync = Stat(patt=6, pdamage_indep=base_internal_stat.special * 0.0886937)

sync_stat = (
    basis_stat + engraving_manager.get_dynamic_modifier(spd=spd + 30, legacy_stack=3)
).add_indep(HyperSync)

logger.info(sync_stat)
nosync_stat = basis_stat + engraving_manager.get_dynamic_modifier(
    spd=spd, legacy_stack=0
)
logger.info(nosync_stat)

RaidMissile = scouter.RaidMissile.build_skill(
    gem=7,
    tripod={
        "오르간 미사일": 4,
        "약점 포착": 4,
    },
    additional_stat=nosync_stat,
)

BabyDrone = scouter.BabyDrone.build_skill(
    gem=0,
    tripod={
        "급소 공격": 4,
        "일제 공격": 5,
    },
    additional_stat=nosync_stat
)

CometStrike = scouter.CometStrike.build_skill(gem=9, additional_stat=sync_stat)
SlugShot = scouter.SlugShot.build_skill(gem=9, additional_stat=sync_stat)
LaserBlade = scouter.LaserBlade.build_skill(gem=9, additional_stat=sync_stat + Stat(pdamage_indep=20))  # Q-E 연계 20%
AccelionBeam = scouter.AccelionBeam.build_skill(gem=9, additional_stat=sync_stat)
BurstBlow = scouter.BurstBlow.build_skill(gem=9, additional_stat=sync_stat)
CrimsonBreaker = scouter.CrimsonBreaker.build_skill(gem=9, additional_stat=sync_stat)

dealcycle = [  # 레미-베드-QESQRWAQEWQRWSQEWAQRW 23s
    RaidMissile,
    BabyDrone,
    CometStrike,
    LaserBlade,
    CrimsonBreaker,
    CometStrike,
    AccelionBeam,
    SlugShot,
    BurstBlow,
    CometStrike,
    LaserBlade,
    SlugShot,
    CometStrike,
    AccelionBeam,
    SlugShot,
    CrimsonBreaker,
    CometStrike,
    LaserBlade,
    SlugShot,
    BurstBlow,
    CometStrike,
    AccelionBeam,
    SlugShot,
]
cycle_time = 23
enemy = Enemy(armor=6000, reduction=23)

calculate(dealcycle, cycle_time, enemy)
