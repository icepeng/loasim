from loasim.core import Skill, Tripod, Stat

RaidMissile = SkillSpecification(
    name="명령 : 레이드 미사일",
    base=3066,
    coefficient=19.10,
    tripods=[
        Tripod(
            "오르간 미사일",
            [
                Stat(pdamage_indep=-30)
                + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-27)
                + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-23)
                + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-19)
                + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-15)
                + Stat(pdamage_indep=100),
            ],
        ),
        Tripod(
            "약점 포착",
            [
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=69),
                Stat(pdamage_indep=78),
                Stat(pdamage_indep=87),
                Stat(pdamage_indep=96),
            ],
        ),
    ],
)

BabyDrone = SkillSpecificationSkill(
    name="명령: 베이비 드론",
    base=3200,
    coefficient=19.71,
    tripods=[
        Tripod(
            "급소 공격",
            [
                Stat(crit=20),
                Stat(crit=26),
                Stat(crit=32),
                Stat(crit=38),
                Stat(crit=45),
            ],
        ),
        Tripod(
            "일제 공격",
            [
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=76),
                Stat(pdamage_indep=85),
                Stat(pdamage_indep=95),
            ],
        ),
    ],
)

CometStrike = Skill(name="코멧 스트라이크", base=1809, coefficient=11.27)
SlugShot = Skill(name="슬러그 샷", base=1841, coefficient=11.50)
LaserBlade = Skill(
    name="레이저 블레이드",
    base=3706.80,
    coefficient=23.13,
)
AccelionBeam = Skill(name="엑셀리온 빔", base=4603, coefficient=28.70, head=True)
BurstBlow = Skill(name="버스트 블로우", base=3488, coefficient=21.71)
CrimsonBreaker = Skill(name="크림슨 브레이커", base=7200, coefficient=44.94)
