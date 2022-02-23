from loasim.core import SkillSpecification, Stat, Tripod

OneStroke = SkillSpecification(
    name="필법 : 한획긋기",
    base=5978,
    coefficient=19.13,
    back=True,
    tripods=[
        Tripod(
            name="급소 타격",
            stat_list=[
                Stat(crit=40),
                Stat(crit=47),
                Stat(crit=54),
                Stat(crit=62),
                Stat(crit=70),
            ],
        ),
        Tripod(
            name="연속 긋기",
            stat_list=[
                Stat(pdamage_indep=40),
                Stat(pdamage_indep=47.2),
                Stat(pdamage_indep=54.4),
                Stat(pdamage_indep=62),
                Stat(pdamage_indep=70),
            ],
        ),
        Tripod(
            name="거대한 붓",
            stat_list=[
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=57),
                Stat(pdamage_indep=64),
                Stat(pdamage_indep=72),
                Stat(pdamage_indep=80),
            ],
        ),
        Tripod(
            name="강화된 일격",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=77),
                Stat(pdamage_indep=86),
                Stat(pdamage_indep=95),
            ],
        ),
    ],
)

Cranes = SkillSpecification(
    name="묵법 : 두루미나래",
    base=5988,
    coefficient=19.16,
    tripods=[
        Tripod(
            name="치명적인 일격",
            stat_list=[
                Stat(crit_damage=100),
                Stat(crit_damage=115),
                Stat(crit_damage=130),
                Stat(crit_damage=145),
                Stat(crit_damage=160),
            ],
        ),
        Tripod(
            name="학익진",
            stat_list=[
                Stat(pdamage_indep=70),
                Stat(pdamage_indep=78),
                Stat(pdamage_indep=87),
                Stat(pdamage_indep=96),
                Stat(pdamage_indep=105),
            ],
        ),
        Tripod(
            name="두루미 폭격",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=77),
                Stat(pdamage_indep=86),
                Stat(pdamage_indep=95),
            ],
        ),
    ],
)

Tiger = SkillSpecification(
    name="묵법 : 범가르기",
    base=5169,
    coefficient=16.54,
    back=True,
    tripods=[
        Tripod(
            name="궤뚫는 일격",
            stat_list=[
                Stat(armor_ignore=50),
                Stat(armor_ignore=57.5),
                Stat(armor_ignore=65),
                Stat(armor_ignore=72.5),
                Stat(armor_ignore=80),
            ],
        ),
        Tripod(
            name="무력화 강화",
            stat_list=[
                Stat(pdamage_indep=20),
                Stat(pdamage_indep=26),
                Stat(pdamage_indep=32),
                Stat(pdamage_indep=38),
                Stat(pdamage_indep=45),
            ],
        ),
        Tripod(
            name="어둠의 기운",
            stat_list=[
                Stat(crit=35),
                Stat(crit=42),
                Stat(crit=49),
                Stat(crit=57),
                Stat(crit=65),
            ],
        ),
        Tripod(
            name="두 마리의 호랑이",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=77),
                Stat(pdamage_indep=86),
                Stat(pdamage_indep=95),
            ],
        ),
        Tripod(
            name="강화된 일격",
            stat_list=[
                Stat(pdamage_indep=80),
                Stat(pdamage_indep=90),
                Stat(pdamage_indep=100),
                Stat(pdamage_indep=110),
                Stat(pdamage_indep=120),
            ],
        ),
    ],
)

Moon = SkillSpecification(
    name="묵법 : 달그리기",
    base=5070,
    coefficient=16.25,
    tripods=[
        Tripod(
            name="별 그리기",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=77),
                Stat(pdamage_indep=86),
                Stat(pdamage_indep=95),
            ],
        ),
        Tripod(
            name="먹물 세례",
            stat_list=[
                Stat(pdamage_indep=10 * 2),
                Stat(pdamage_indep=13 * 2),
                Stat(pdamage_indep=16 * 2),
                Stat(pdamage_indep=19 * 2),
                Stat(pdamage_indep=22.5 * 2),
            ],
        ),
        Tripod(
            name="검은 달",
            stat_list=[
                Stat(pdamage_indep=20),
                Stat(pdamage_indep=26),
                Stat(pdamage_indep=32),
                Stat(pdamage_indep=38),
                Stat(pdamage_indep=45),
            ],
        ),
        Tripod(
            name="붉은 달",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=77),
                Stat(pdamage_indep=86),
                Stat(pdamage_indep=95),
            ],
        ),
    ],
)

InkRise = SkillSpecification(
    name="묵법 : 먹오름",
    base=478,
    coefficient=1.55,
    multiplier=8,
    tripods=[
        Tripod(
            name="치명적인 일격",
            stat_list=[
                Stat(crit_damage=40),
                Stat(crit_damage=52.5),
                Stat(crit_damage=65),
                Stat(crit_damage=77.5),
                Stat(crit_damage=90),
            ],
        ),
        Tripod(
            name="헤어날 수 없는 늪",
            stat_list=[
                Stat(pdamage_indep=60),
                Stat(pdamage_indep=68),
                Stat(pdamage_indep=77),
                Stat(pdamage_indep=86),
                Stat(pdamage_indep=95),
            ],
        ),
        Tripod(
            name="먹물점정",
            stat_list=[
                Stat(pdamage_indep=80),
                Stat(pdamage_indep=89.6),
                Stat(pdamage_indep=99.2),
                Stat(pdamage_indep=109.6),
                Stat(pdamage_indep=120),
            ],
        ),
    ],
)
