from collections import defaultdict
from loasim.CharacterModifier import CharacterModifier, Stat
from loasim.Enemy import Enemy
from loasim.Skill import Skill

base_stat = Stat(weapon_att=28800, stat_main=119610, crit=537, special=56, swift=1691)
spd = base_stat.get_spd() + 10  # 갈망 +10

base_mdf = base_stat.get_mdf()
weapon_mdf = CharacterModifier(pdamage=21.86)  # 무기 품질

Grudge3 = CharacterModifier(pdamage_indep=20)
StabilizedStatus3 = CharacterModifier(pdamage_indep=16)
RaidCaptain2 = CharacterModifier(pdamage_indep=spd * 0.22)
RaidCaptain3 = CharacterModifier(pdamage_indep=spd * 0.45)
KeenBluntWeapon3 = CharacterModifier(pdamage_indep=-2, crit_damage=50)
CursedDoll3 = CharacterModifier(patt=16)
Adrenaline1 = CharacterModifier(patt=1.8, crit=5)
Adrenaline2 = CharacterModifier(patt=3.6, crit=10)
Adrenaline3 = CharacterModifier(patt=6, crit=15)
Recurrence1 = CharacterModifier(crit=6, crit_damage=20)
Recurrence3 = CharacterModifier(crit=12, crit_damage=40)

Nightmare2 = CharacterModifier(pdamage_indep=12)  # 악몽2셋
Domination4 = CharacterModifier(pdamage_indep=25)  # 지배4셋

Card = CharacterModifier(crit=7)  # 남바절

SunDrawBuff = CharacterModifier(crit=49.7)  # 나만의 권능 5
SunWellBuff = CharacterModifier(patt=30)  # 나만의 우물

Engraving1 = Grudge3 + KeenBluntWeapon3 + CursedDoll3 + RaidCaptain3 + Recurrence3  # 원예저돌회
Engraving2 = Grudge3 + KeenBluntWeapon3 + CursedDoll3 + StabilizedStatus3 + RaidCaptain2 + Recurrence1  # 원예저안돌회
Engraving3 = Grudge3 + KeenBluntWeapon3 + StabilizedStatus3 + RaidCaptain3 + Recurrence3  # 원예안돌회
Engraving4 = Grudge3 + KeenBluntWeapon3 + Adrenaline3 + RaidCaptain3 + Recurrence3  # 원예아돌회
Engraving5 = Grudge3 + KeenBluntWeapon3 + CursedDoll3 + RaidCaptain3 + Adrenaline2 + Recurrence1  # 원예저돌아회
Engraving6 = Grudge3 + CursedDoll3 + StabilizedStatus3 + RaidCaptain3 + Recurrence3  # 원저안돌회

base_mdf = (
    base_mdf
    + weapon_mdf
    + Nightmare2
    + Domination4
    + Engraving3
    + Card
)
static_mdf = base_mdf.add_indep(SunDrawBuff + SunWellBuff)

OneStrokeGem = CharacterModifier(pdamage_indep=21)  # 7레벨 멸화
OneStrokeTripod = CharacterModifier(pdamage_indep=80) + CharacterModifier(pdamage_indep=95)  # 거대한 붓 5, 강화된 일격 5
OneStroke = Skill("필법 : 한획긋기", base=5978, coefficient=19.13, mdf=static_mdf + OneStrokeGem + OneStrokeTripod)

CranesGem = CharacterModifier(pdamage_indep=15)  # 5레벨 멸화
CranesTripod = CharacterModifier(crit_damage=160) + CharacterModifier(pdamage_indep=105)  # 치명적인 일격 5, 학익진 5
Cranes = Skill("묵법 : 두루미나래", base=5988, coefficient=19.16, mdf=static_mdf + CranesGem + CranesTripod)

TigerGem = CharacterModifier(pdamage_indep=18)  # 6레벨 멸화
TigerTripod = CharacterModifier(armor_ignore=80) + CharacterModifier(pdamage_indep=120)  # 궤뚫는 일격 5, 강화된 일격 5
Tiger = Skill("묵법 : 범가르기", base=5169, coefficient=16.54, mdf=static_mdf + TigerGem + TigerTripod)

MoonGem = CharacterModifier(pdamage_indep=21)  # 7레벨 멸화
MoonTripod = CharacterModifier(pdamage_indep=86) + CharacterModifier(pdamage_indep=86)  # 별 그리기 4, 붉은 달 4
Moon = Skill("묵법 : 달그리기", base=5070, coefficient=16.25, mdf=static_mdf + MoonGem + MoonTripod)

InkRiseGem = CharacterModifier(pdamage_indep=15)  # 5레벨 멸화
InkRiseTripod = CharacterModifier(crit_damage=40) + CharacterModifier(pdamage_indep=80)  # 치명적인 일격 1, 먹물점정 1
InkRise = Skill("묵법 : 먹오름", base=478, coefficient=1.55, multiplier=8, mdf=static_mdf + InkRiseGem + InkRiseTripod)

dealcycle = [
    OneStroke,
    Cranes,
    Tiger,
    Moon,
    InkRise,
]
cycle_time = 12.127

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