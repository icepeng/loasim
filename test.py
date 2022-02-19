from collections import defaultdict
from loasim.CharacterModifier import CharacterModifier, Stat
from loasim.Enemy import Enemy
from loasim.Skill import Skill

base_stat = Stat(weapon_att=50362, stat_main=156350, crit=632, special=1776, swift=53)
spd = base_stat.get_spd() + 10  # 갈망 +10

base_mdf = base_stat.get_mdf()
weapon_mdf = CharacterModifier(pdamage=23.45)  # 무기 품질

Grudge3 = CharacterModifier(pdamage_indep=20)
Barricade3 = CharacterModifier(pdamage_indep=16)
RaidCaptain3 = CharacterModifier(pdamage_indep=spd * 0.45)
RaidCaptain3_Sync = CharacterModifier(pdamage_indep=(spd + 30) * 0.45)
KeenBluntWeapon3 = CharacterModifier(pdamage_indep=-2, crit_damage=50)
CursedDoll3 = CharacterModifier(patt=16)
Adrenaline1 = CharacterModifier(patt=1.8, crit=5)
Adrenaline2 = CharacterModifier(patt=3.6, crit=10)
Adrenaline3 = CharacterModifier(patt=6, crit=15)
Legacy1 = CharacterModifier(pdamage_indep=6)
Legacy3 = CharacterModifier(pdamage_indep=18)

Illusion6 = CharacterModifier(pdamage_indep=29, crit=18 + 7)  # 환각6셋
HyperSync = CharacterModifier(patt=6, pdamage_indep=base_stat.special * 0.0886937)

Card = CharacterModifier(crit=7)  # 남바절

SyncGem = CharacterModifier(pdamage_indep=30)  # 9레벨 멸화

static_mdf = (
    base_mdf
    + weapon_mdf
    + Illusion6
    + Grudge3
    + Barricade3
    + KeenBluntWeapon3
    + Adrenaline2
    + Card
)
sync_mdf = static_mdf.add_indep(RaidCaptain3_Sync + Legacy1 + HyperSync + SyncGem)
nosync_mdf = static_mdf.add_indep(RaidCaptain3)

RaidMissileGem = CharacterModifier(pdamage_indep=21)  # 7레벨 멸화
RaidMissileTripod = CharacterModifier(pdamage_indep=62) + CharacterModifier(pdamage_indep=87)  # 오르간 미사일 4, 약점 포착 4
RaidMissile = Skill("레이드 미사일", base=3066, coefficient=19.10, mdf=nosync_mdf + RaidMissileGem + RaidMissileTripod)

BabyDroneTripod = CharacterModifier(crit=38) + CharacterModifier(pdamage_indep=95)  # 급소 공격 4, 일제 공격 5
BabyDrone = Skill("베이비 드론", base=3200, coefficient=19.71, mdf=nosync_mdf + BabyDroneTripod)

CometStrike = Skill("코멧 스트라이크", base=1809, coefficient=11.27, mdf=sync_mdf)
SlugShot = Skill("슬러그 샷", base=1841, coefficient=11.50, mdf=sync_mdf)
LaserBlade = Skill(
    "레이저 블레이드",
    base=3706.80,
    coefficient=23.13,
    mdf=sync_mdf + CharacterModifier(pdamage_indep=20),
)
AccelionBeam = Skill("엑셀리온 빔", base=4603, coefficient=28.70, mdf=sync_mdf)
BurstBlow = Skill("버스트 블로우", base=3488, coefficient=21.71, mdf=sync_mdf)
CrimsonBreaker = Skill("크림슨 브레이커", base=7200, coefficient=44.94, mdf=sync_mdf)

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

total_damage = 0
damage_dict = defaultdict(float)
for sk in dealcycle:
    damage = sk.get_damage(enemy)
    total_damage += damage
    damage_dict[sk.name] += damage

for sk, dmg in damage_dict.items():
    print(sk, f"{dmg / total_damage *100:,.3f}%")
print(f"total damage: {total_damage:,.0f}")
print(f"dps: {total_damage / cycle_time:,.0f}")