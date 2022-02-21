from loasim.core import SkillSpecification, Stat, Tripod

RaidMissile = SkillSpecification(
    name="명령 : 레이드 미사일",
    base=3066,
    coefficient=19.10,
    tripods=[
        Tripod(
            name="오르간 미사일",
            stat_list=[
                Stat(pdamage_indep=-30) + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-27) + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-23) + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-19) + Stat(pdamage_indep=100),
                Stat(pdamage_indep=-15) + Stat(pdamage_indep=100),
            ],
        ),
        Tripod(
            name="약점 포착",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=69),
                Stat(pdamage_indep=78),
                Stat(pdamage_indep=87),
                Stat(pdamage_indep=96),
            ],
        ),
    ],
)

BabyDrone = SkillSpecification(
    name="명령: 베이비 드론",
    base=3200,
    coefficient=19.71,
    tripods=[
        Tripod(
            name="급소 공격",
            stat_list=[
                Stat(crit=20),
                Stat(crit=26),
                Stat(crit=32),
                Stat(crit=38),
                Stat(crit=45),
            ],
        ),
        Tripod(
            name="일제 공격",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=76),
                Stat(pdamage_indep=85),
                Stat(pdamage_indep=95),
            ],
        ),
    ],
)

CometStrike = SkillSpecification(name="코멧 스트라이크", base=1809, coefficient=11.27)
SlugShot = SkillSpecification(name="슬러그 샷", base=1841, coefficient=11.50)
LaserBlade = SkillSpecification(
    name="레이저 블레이드",
    base=3706.80,
    coefficient=23.13,
)
AccelionBeam = SkillSpecification(
    name="엑셀리온 빔", base=4603, coefficient=28.70, head=True
)
BurstBlow = SkillSpecification(name="버스트 블로우", base=3488, coefficient=21.71)
CrimsonBreaker = SkillSpecification(name="크림슨 브레이커", base=7200, coefficient=44.94)
