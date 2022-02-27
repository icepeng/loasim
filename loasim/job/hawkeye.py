from loasim.core import SkillSpecification, Stat, Tripod
from loasim.core.skill import SkillRepository

lostark_hawkeye_skill_repository = SkillRepository()

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="스나이프",
        type="Holding",
        damage_table={
            10: (5033, 27.33895),
            11: (5035, 29.74807),
            12: (5037, 31.22183),
        },
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
)

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="샤프 슈터",
        type="Normal",
        damage_table={
            10: (887, 4.84482),
            11: (887, 5.27079),
            12: (888, 5.53278),
        },
        multiplier=3,
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
                    Stat(pdamage_indep=(500 - 300) / 3, crit_damage=50),
                    Stat(pdamage_indep=(500 - 300) / 3, crit_damage=62),
                    Stat(pdamage_indep=(500 - 300) / 3, crit_damage=74),
                    Stat(pdamage_indep=(500 - 300) / 3, crit_damage=87),
                    Stat(pdamage_indep=(500 - 300) / 3, crit_damage=100),
                ],
            ),
        ],
    )
)

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="차징 샷",
        type="Charge",
        damage_table={
            10: (3384, 18.37030),
            11: (3385, 19.98427),
            12: (3386, 20.97922),
        },
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
                stat_list=[
                    Stat(pdamage_indep=50),
                    Stat(pdamage_indep=54),
                    Stat(pdamage_indep=58),
                    Stat(pdamage_indep=62),
                    Stat(pdamage_indep=66.5),
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
)

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="애로우 해일",
        type="Normal",
        damage_table={
            10: (378, 2.03892),
            11: (378, 2.21791),
            12: (378, 2.32789),
        },
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
)

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="아토믹 애로우",
        type="Normal",
        damage_table={
            10: (142, 0.77697),
            11: (142, 0.84498),
            12: (142, 0.88700),
        },
        tripods=[
            Tripod(
                name="전격 화살",
                skill_after="아토믹 애로우(전격)",
            ),
            Tripod(name="화살촉 강화"),
            Tripod(name="긴 도화선"),
        ],
        skill_afters=["아토믹 애로우(폭발)"],
    )
)

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="아토믹 애로우(폭발)",
        type="Normal",
        damage_table={
            10: (1052, 5.71679),
            11: (1052, 6.21874),
            12: (1053, 6.52875),
        },
        tripods=[
            Tripod(
                name="전격 화살",
            ),
            Tripod(
                name="화살촉 강화",
                stat_list=[
                    Stat(crit=30),
                    Stat(crit=37.5),
                    Stat(crit=45),
                    Stat(crit=52.5),
                    Stat(crit=60),
                ],
            ),
            Tripod(
                name="긴 도화선",
                stat_list=[
                    Stat(pdamage_indep=75),
                    Stat(pdamage_indep=85),
                    Stat(pdamage_indep=95),
                    Stat(pdamage_indep=105),
                    Stat(pdamage_indep=116),
                ],
            ),
        ],
    )
)

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="아토믹 애로우(전격)",
        type="Normal",
        damage_table={
            10: (1052, 5.71679),
            11: (1052, 6.21874),
            12: (1053, 6.52875),
        },
        multiplier=3,
        tripods=[
            Tripod(
                name="전격 화살",
                stat_list=[
                    Stat(pdamage_indep=15.53 - 100),
                    Stat(pdamage_indep=18.33 - 100),
                    Stat(pdamage_indep=21.28 - 100),
                    Stat(pdamage_indep=24.23 - 100),
                    Stat(pdamage_indep=27.18 - 100),
                ],
            ),
        ],
    )
)

lostark_hawkeye_skill_repository.add(
    SkillSpecification(
        name="애로우 샤워",
        type="Area",
        damage_table={
            10: (413, 2.24392),
            11: (413, 2.44091),
            12: (414, 2.56289),
        },
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
)
