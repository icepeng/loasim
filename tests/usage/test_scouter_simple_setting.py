from loguru import logger

from loasim.calculate import calculate
from loasim.card import lostark_default_card_repository
from loasim.core import Enemy, InternalStat, Stat
from loasim.Engraving import EngravingManager
from loasim.job.scouter import lostark_scouter_skill_repository
from loasim.setitem import SetItemState, lostark_setitem_repository

base_internal_stat = InternalStat(
    weapon_att=50362, stat_main=156350, crit=632, special=1776, swift=53
)
spd = base_internal_stat.get_spd() + 10  # 갈망 +10

base_stat = base_internal_stat.get_stat()
weapon_stat = Stat(pdamage=23.45)  # 무기 품질

logger.info(base_stat)
logger.info(weapon_stat)

setitem_state = [
    SetItemState(
        name="환각",
        level_1=6,
        level_2=6,
    )
]

engraving_manager = EngravingManager(
    ("원한", 3), ("예리한 둔기", 3), ("바리케이드", 3), ("돌격대장", 3), ("아드레날린", 3), ("진화의 유산", 1)
)
card = lostark_default_card_repository.get("남겨진 바람의 절벽 (12)")

basis_stat = (
    base_stat
    + weapon_stat
    + lostark_setitem_repository.get_stat(setitem_state)
    + engraving_manager.get_static_modifier()
    + card.stat
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

RaidMissile = lostark_scouter_skill_repository.build(
    name="명령 : 레이드 미사일",
    level=12,
    gem=7,
    tripod={
        "오르간 미사일": 4,
        "약점 포착": 4,
    },
    additional_stat=nosync_stat,
)

BabyDrone = lostark_scouter_skill_repository.build(
    name="명령 : 베이비 드론",
    level=12,
    gem=0,
    tripod={
        "급소 공격": 4,
        "일제 공격": 5,
    },
    additional_stat=nosync_stat,
)

CometStrike = lostark_scouter_skill_repository.build(
    name="코멧 스트라이크",
    level=12,
    gem=9,
    additional_stat=sync_stat,
)
SlugShot = lostark_scouter_skill_repository.build(
    name="슬러그 샷",
    level=12,
    gem=9,
    additional_stat=sync_stat,
)
LaserBlade = lostark_scouter_skill_repository.build(
    name="레이저 블레이드",
    level=12,
    gem=9,
    additional_stat=sync_stat + Stat(pdamage_indep=20),  # Q-E 연계 20%
)
AccelionBeam = lostark_scouter_skill_repository.build(
    name="엑셀리온 빔",
    level=12,
    gem=9,
    additional_stat=sync_stat,
)
BurstBlow = lostark_scouter_skill_repository.build(
    name="버스트 블로우",
    level=12,
    gem=9,
    additional_stat=sync_stat,
)
CrimsonBreaker = lostark_scouter_skill_repository.build(
    name="크림슨 브레이커",
    level=12,
    gem=9,
    additional_stat=sync_stat,
)

dealcycle = [  # 레미-베드-QESQRWAQEWQRWSQEWAQRW 23s
    (RaidMissile, None),
    (BabyDrone, None),
    (CometStrike, None),
    (LaserBlade, None),
    (CrimsonBreaker, None),
    (CometStrike, None),
    (AccelionBeam, None),
    (SlugShot, None),
    (BurstBlow, None),
    (CometStrike, None),
    (LaserBlade, None),
    (SlugShot, None),
    (CometStrike, None),
    (AccelionBeam, None),
    (SlugShot, None),
    (CrimsonBreaker, None),
    (CometStrike, None),
    (LaserBlade, None),
    (SlugShot, None),
    (BurstBlow, None),
    (CometStrike, None),
    (AccelionBeam, None),
    (SlugShot, None),
]
cycle_time = 23
enemy = Enemy(armor=6000, reduction=23)

calculate(dealcycle, cycle_time, enemy)
