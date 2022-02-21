from calculate import calculate
from loasim.CharacterModifier import CharacterModifier, Stat
from loasim.Enemy import Enemy
from loasim.SetItem import SetItemManager
from loasim.Skill import SkillWrapper
from loasim.Engraving import EngravingManager
from loasim.Card import CardManager
from loasim import scouter

base_stat = Stat(weapon_att=50362, stat_main=156350, crit=632, special=1776, swift=53)
spd = base_stat.get_spd() + 10  # 갈망 +10

base_mdf = base_stat.get_mdf()
weapon_mdf = CharacterModifier(pdamage=23.45)  # 무기 품질

set_item_manager = SetItemManager(("환각", 6, 6))
engraving_manager = EngravingManager(
    ("원한", 3), ("예리한 둔기", 3), ("바리케이드", 3), ("돌격대장", 3), ("아드레날린", 3), ("진화의 유산", 1)
)
card_manager = CardManager("남겨진 바람의 절벽 (12)")

static_mdf = (
    base_mdf
    + weapon_mdf
    + set_item_manager.get_static_modifier()
    + engraving_manager.get_static_modifier()
    + card_manager.get_static_modifier()
)

HyperSync = CharacterModifier(patt=6, pdamage_indep=base_stat.special * 0.0886937)
sync_mdf = (
    static_mdf + engraving_manager.get_dynamic_modifier(spd=spd + 30, legacy_stack=3)
).add_indep(HyperSync)
nosync_mdf = static_mdf + engraving_manager.get_dynamic_modifier(
    spd=spd, legacy_stack=0
)

RaidMissile = SkillWrapper(
    scouter.RaidMissile.set_gem(7).set_tripod("오르간 미사일", 4).set_tripod("약점 포착", 4),
    mdf=nosync_mdf,
)
BabyDrone = SkillWrapper(
    scouter.BabyDrone.set_tripod("급소 공격", 4).set_tripod("일제 공격", 5), mdf=nosync_mdf
)

CometStrike = SkillWrapper(scouter.CometStrike.set_gem(9), mdf=sync_mdf)
SlugShot = SkillWrapper(scouter.SlugShot.set_gem(9), mdf=sync_mdf)
LaserBlade = SkillWrapper(
    scouter.LaserBlade.set_gem(9), mdf=sync_mdf + CharacterModifier(pdamage_indep=20)
)  # Q-E 연계 20%
AccelionBeam = SkillWrapper(scouter.AccelionBeam.set_gem(9), mdf=sync_mdf)
BurstBlow = SkillWrapper(scouter.BurstBlow.set_gem(9), mdf=sync_mdf)
CrimsonBreaker = SkillWrapper(scouter.CrimsonBreaker.set_gem(9), mdf=sync_mdf)

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
