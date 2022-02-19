from collections import defaultdict
from loasim.CharacterModifier import CharacterModifier, Stat
from loasim.Enemy import Enemy
from loasim.Skill import Skill

# base_stat = Stat(weapon_att=50362, stat_main=156350, crit=607, special=56, swift=1756)
base_stat = Stat(weapon_att=31392, stat_main=133748, crit=607, special=56, swift=1756)
# base_stat = Stat(weapon_att=31392, stat_main=133748, crit=1800, special=0, swift=0)

base_mdf = base_stat.get_mdf()
weapon_mdf = CharacterModifier(pdamage=23.45)  # 무기 품질

Grudge3 = CharacterModifier(pdamage_indep=20)
HitMaster3 = CharacterModifier(pdamage_indep=16)
KeenBluntWeapon3 = CharacterModifier(pdamage_indep=-2, crit_damage=50)
CursedDoll3 = CharacterModifier(patt=16)
Adrenaline3 = CharacterModifier(patt=6, crit=15)
PreciseDagger = CharacterModifier(crit=20, crit_damage=-12)

Nightmare2 = CharacterModifier(pdamage_indep=12)  # 악몽2셋
Domination4 = CharacterModifier(pdamage_indep=25)  # 지배4셋

Card = CharacterModifier(crit=7)  # 남바절
AtomicArrowSynergy = CharacterModifier(pdamage_indep=6)

static_mdf = (
    base_mdf
    + weapon_mdf
    + Nightmare2
    + Domination4
    + Grudge3
    + HitMaster3
    + KeenBluntWeapon3
    + Adrenaline3
    + PreciseDagger
    + Card
    + AtomicArrowSynergy
)

SnipeGem = CharacterModifier(pdamage_indep=21)  # 7레벨 멸화
SnipeTripod = CharacterModifier(pdamage_indep=145) + CharacterModifier(crit=30, crit_damage=160)  # 약점 포착 5, 손쉬운 먹잇감 5
Snipe = Skill("스나이프", base=5037, coefficient=31.22, mdf=static_mdf + SnipeGem + SnipeTripod)

SharpShooterGem = CharacterModifier(pdamage_indep=21)  # 7레벨 멸화
SharpShooterTripod = CharacterModifier(crit=40) + CharacterModifier(pdamage_indep=70) + CharacterModifier(crit_damage=100)  # 급소 타격 5, 약점 포착 5, 집중 사격 5
SharpShooter = Skill("샤프 슈터", base=888, coefficient=5.53, multiplier=5, mdf=static_mdf + SharpShooterGem + SharpShooterTripod)

ChargingShotGem = CharacterModifier(pdamage_indep=15)  # 5레벨 멸화
ChargingShotTripod = CharacterModifier(pdamage_indep=72) + CharacterModifier(pdamage_indep=50)  # 더블 샷 4, 즉발 4 - 더블샷, 즉발 같이 사용시 즉발 1렙으로 적용되는 버그있음
ChargingShot = Skill("차징 샷", base=3386, coefficient=20.98, mdf=static_mdf + ChargingShotGem + ChargingShotTripod)

ArrowWaveGem = CharacterModifier(pdamage_indep=21)  # 7레벨 멸화
ArrowWaveTripod = CharacterModifier(crit=33) + CharacterModifier(pdamage_indep=80) + CharacterModifier(pdamage_indep=245)  # 강화된 화살 4, 저속 탄환 5, 웨이브 해일 5
ArrowWave = Skill("애로우 해일", base=378, coefficient=2.33, multiplier=4, mdf=static_mdf + ArrowWaveGem + ArrowWaveTripod)

AtomicArrowGem = CharacterModifier(pdamage_indep=15)  # 5레벨 멸화
AtomicArrow = Skill("아토믹 애로우", base=142, coefficient=0.89, mdf=static_mdf + AtomicArrowGem)
AtomicArrowExplode = Skill("아토믹 애로우(폭발)", base=1053, coefficient=6.53, mdf=static_mdf + AtomicArrowGem)
AtomicArrowElectric = Skill("아토믹 애로우(전격)", base=166, coefficient=1.59, multiplier=3, mdf=static_mdf + AtomicArrowGem)

ArrowShowerGem = CharacterModifier(pdamage_indep=15)  # 5레벨 멸화
ArrowShowerTripod = CharacterModifier(pdamage_indep=110)  # 지속력 강화 4
ArrowShower = Skill("애로우 샤워", base=413, coefficient=2.24, multiplier=5, mdf=static_mdf + ArrowShowerGem + ArrowShowerTripod)

dealcycle = [  # 62s
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowShower,
    ArrowWave,
    SharpShooter,
    Snipe,
    ChargingShot,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowShower,
    ArrowWave,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    SharpShooter,
    Snipe,
    ChargingShot,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowShower,
    ArrowWave,
    SharpShooter,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    Snipe,
    ChargingShot,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowShower,
    ArrowWave,
    SharpShooter,
    Snipe,
    ChargingShot,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowShower,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowWave,
    Snipe,
    SharpShooter,
    ChargingShot,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowShower,
    ArrowWave,
    Snipe,
    SharpShooter,
    ChargingShot,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    ArrowShower,
    ArrowWave,
    AtomicArrow,
    AtomicArrowExplode,
    AtomicArrowElectric,
    Snipe,
    SharpShooter,
    ChargingShot,
]
cycle_time = 62

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