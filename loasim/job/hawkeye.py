from loasim.core import SkillSpecification, Stat, Tripod

Snipe = SkillSpecification(
    name="스나이프",
    base=5037,
    coefficient=31.22,
    tripods=[
        Tripod(
            name="약점 포착",
            stat_list=[
                Stat(pdamage_indep=100),
                Stat(pdamage_indep=111),
                Stat(pdamage_indep=122),
                Stat(pdamage_indep=133),
                Stat(pdamage_indep=145),
            ],
        ),
        Tripod(
            name="손쉬운 먹잇감",
            stat_list=[
                Stat(crit=30, crit_damage=100),
                Stat(crit=30, crit_damage=115),
                Stat(crit=30, crit_damage=130),
                Stat(crit=30, crit_damage=145),
                Stat(crit=30, crit_damage=160),
            ],
        ),
    ],
)

SharpShooter = SkillSpecification(
    name="샤프 슈터",
    base=888,
    coefficient=5.53,
    multiplier=5,
    tripods=[
        Tripod(
            name="급소 타격",
            stat_list=[
                Stat(crit=15),
                Stat(crit=21),
                Stat(crit=27),
                Stat(crit=33),
                Stat(crit=40),
            ],
        ),
        Tripod(
            name="약점 포착",
            stat_list=[
                Stat(pdamage_indep=40),
                Stat(pdamage_indep=47.2),
                Stat(pdamage_indep=54.8),
                Stat(pdamage_indep=62.4),
                Stat(pdamage_indep=70),
            ],
        ),
        Tripod(
            name="집중 사격",
            stat_list=[
                Stat(crit_damage=50),
                Stat(crit_damage=62),
                Stat(crit_damage=74),
                Stat(crit_damage=87),
                Stat(crit_damage=100),
            ],
        ),
    ],
)

ChargingShot = SkillSpecification(
    name="차징 샷",
    base=3386,
    coefficient=20.98,
    tripods=[
        Tripod(
            name="더블 샷",
            stat_list=[
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=57),
                Stat(pdamage_indep=64),
                Stat(pdamage_indep=72),
                Stat(pdamage_indep=80),
            ],
        ),
        Tripod(
            name="즉발",
            stat_list=[  # 더블샷, 즉발 같이 사용시 즉발 1렙으로 적용되는 버그있음
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=50),
            ],
        ),
        Tripod(
            name="정조준",
            stat_list=[
                Stat(crit=50, pdamage_indep=30),
                Stat(crit=50, pdamage_indep=37),
                Stat(crit=50, pdamage_indep=44),
                Stat(crit=50, pdamage_indep=52),
                Stat(crit=50, pdamage_indep=60),
            ],
        ),
    ],
)

ArrowWave = SkillSpecification(
    name="애로우 해일",
    base=378,
    coefficient=2.33,
    multiplier=4,
    tripods=[
        Tripod(
            name="강화된 화살",
            stat_list=[
                Stat(crit=15),
                Stat(crit=21),
                Stat(crit=27),
                Stat(crit=33),
                Stat(crit=40),
            ],
        ),
        Tripod(
            name="저속 탄환",  # 웨이브 해일 적용 기준
            stat_list=[
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=57),
                Stat(pdamage_indep=64),
                Stat(pdamage_indep=72),
                Stat(pdamage_indep=80),
            ],
        ),
        Tripod(
            name="재빠른 발사",
            stat_list=[
                Stat(crit_damage=60),
                Stat(crit_damage=75),
                Stat(crit_damage=90),
                Stat(crit_damage=105),
                Stat(crit_damage=120),
            ],
        ),
        Tripod(
            name="웨이브 해일",
            stat_list=[
                Stat(pdamage_indep=200),
                Stat(pdamage_indep=215),
                Stat(pdamage_indep=230),
                Stat(pdamage_indep=245),
                Stat(pdamage_indep=260),
            ],
        ),
    ],
)

AtomicArrow = SkillSpecification(
    name="아토믹 애로우",
    base=142,
    coefficient=0.89,
    tripods=[],
)

AtomicArrowExplode = SkillSpecification(
    name="아토믹 애로우(폭발)",
    base=1053,
    coefficient=6.53,
    tripods=[],
)

AtomicArrowElectric = SkillSpecification(
    name="아토믹 애로우(전격)", base=166, coefficient=1.59, multiplier=3, tripods=[]
)

ArrowShower = SkillSpecification(
    name="애로우 샤워",
    base=413,
    coefficient=2.24,
    multiplier=5,
    tripods=[
        Tripod(
            name="지속력 강화",
            stat_list=[
                Stat(pdamage_indep=80),
                Stat(pdamage_indep=90),
                Stat(pdamage_indep=100),
                Stat(pdamage_indep=110),
                Stat(pdamage_indep=120),
            ],
        ),
        Tripod(
            name="장대비",  # 지속력 강화 적용 기준
            stat_list=[
                Stat(pdamage_indep=20 * 10 / 5),
                Stat(pdamage_indep=23.4 * 10 / 5),
                Stat(pdamage_indep=26.8 * 10 / 5),
                Stat(pdamage_indep=30.4 * 10 / 5),
                Stat(pdamage_indep=34 * 10 / 5),
            ],
        ),
    ],
)
