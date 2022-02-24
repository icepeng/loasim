from loasim.core import SkillSpecification, Stat, Tripod

SpinCutter = SkillSpecification(  # TODO: 횟수 조절은 어떻게?
    name="스핀 커터",
    damage_table={
        10: (641, 3.450),
    },
    back=True,
    tripods=[],
)

DarkAccel = SkillSpecification(
    name="다크 악셀",
    damage_table={
        10: (1535, 8.926),
    },
    back=True,
    tripods=[],
)

SoulAbsorber = SkillSpecification(
    name="소울 앱소버",
    damage_table={
        10: (3176, 17.217),
        11: (3178, 18.731),
        12: (3179, 19.663),
    },
    back=True,
    tripods=[
        Tripod(
            name="암흑 공격",
            stat_list=[
                Stat(pdamage_indep=30),
                Stat(pdamage_indep=37),
                Stat(pdamage_indep=44),
                Stat(pdamage_indep=52),
                Stat(pdamage_indep=60),
            ],
        ),
        Tripod(
            name="화염 공격",
            stat_list=[
                Stat(crit=30),
                Stat(crit=37),
                Stat(crit=44),
                Stat(crit=52),
                Stat(crit=60),
            ],
        ),
        Tripod(
            name="강력한 찌르기",
            stat_list=[
                Stat(crit_damage=50),
                Stat(crit_damage=62),
                Stat(crit_damage=74),
                Stat(crit_damage=87),
                Stat(crit_damage=100),
            ],
        ),
        Tripod(
            name="반 가르기",
            stat_list=[
                Stat(pdamage_indep=100),
                Stat(pdamage_indep=110),
                Stat(pdamage_indep=120),
                Stat(pdamage_indep=130),
                Stat(pdamage_indep=144),
            ],
        ),
    ],
)

EarthSlash = SkillSpecification(
    name="어스 슬래쉬",
    damage_table={
        10: (1899, 10.317),
    },
    head=True,
    back=True,
    tripods=[
        Tripod(
            name="약점 포착",
            stat_list=[
                Stat(pdamage_indep=40),
                Stat(pdamage_indep=47.2),
                Stat(pdamage_indep=54.8),
                Stat(pdamage_indep=62.4),
                Stat(pdamage_indep=70),
            ],
        )
    ],
)

EarthSlashPush = SkillSpecification(
    name="어스 슬래쉬(밀어내기)",
    damage_table={
        10: (1899, 10.317),
    },
    head=True,
    back=True,
    tripods=[
        Tripod(
            name="밀어내기",
            stat_list=[
                Stat(pdamage_indep=15 - 100),
                Stat(pdamage_indep=21.1 - 100),
                Stat(pdamage_indep=27.4 - 100),
                Stat(pdamage_indep=33.8 - 100),
                Stat(pdamage_indep=40 - 100),
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
    ],
)

EarthSlashPush = SkillSpecification(
    name="어스 슬래쉬(대지 폭발)",
    damage_table={
        10: (1899, 10.317),
    },
    head=True,
    back=True,
    tripods=[
        Tripod(
            name="대지 폭발",
            stat_list=[
                Stat(pdamage_indep=90 - 100),
                Stat(pdamage_indep=99.9 - 100),
                Stat(pdamage_indep=109.8 - 100),
                Stat(pdamage_indep=119.7 - 100),
                Stat(pdamage_indep=129.6 - 100),
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
    ],
)

MoonlightSonic = SkillSpecification(
    name="문라이트 소닉",
    damage_table={
        10: (3647, 19.751),
        11: (3648, 21.485),
        12: (3650, 22.556),
    },
    tripods=[
        Tripod(
            name="암흑 공격",
            stat_list=[
                Stat(pdamage_indep=15),
                Stat(pdamage_indep=21),
                Stat(pdamage_indep=27),
                Stat(pdamage_indep=33),
                Stat(pdamage_indep=40),
            ],
        ),
        Tripod(
            name="지속력 강화",
            stat_list=[
                Stat(pdamage_indep=50),
                Stat(pdamage_indep=56),
                Stat(pdamage_indep=64),
                Stat(pdamage_indep=72),
                Stat(pdamage_indep=80),
            ],
        ),
        Tripod(
            name="집중 공격",
            stat_list=[
                Stat(crit=50),
                Stat(crit=57),
                Stat(crit=64),
                Stat(crit=72),
                Stat(crit=80),
            ],
        ),
        Tripod(
            name="쉐이드 소닉",
            stat_list=[
                Stat(pdamage_indep=70),
                Stat(pdamage_indep=78),
                Stat(pdamage_indep=87),
                Stat(pdamage_indep=96),
                Stat(pdamage_indep=105),
            ],
        ),
    ],
)

Maelstorm = SkillSpecification(
    name="마엘스톰",
    damage_table={
        7: (1023, 6.0648),
    },
    tripods=[],
)

BlitzRush = SkillSpecification(
    name="블리츠 러시",
    damage_table={
        10: (4211, 22.895),
        11: (4213, 24.904),
        12: (4214, 26.144),
    },
    back=True,
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
            name="차지 강화",
            stat_list=[
                Stat(pdamage_indep=20 * 2),
                Stat(pdamage_indep=23 * 2),
                Stat(pdamage_indep=27 * 2),
                Stat(pdamage_indep=31 * 2),
                Stat(pdamage_indep=35 * 2),
            ],
        ),
        Tripod(
            name="쉐도우 러시",
            stat_list=[
                Stat(pdamage_indep=40),
                Stat(pdamage_indep=47),
                Stat(pdamage_indep=54),
                Stat(pdamage_indep=62),
                Stat(pdamage_indep=70),
            ],
        ),
        Tripod(
            name="듀얼 블리츠",
            stat_list=[
                Stat(pdamage_indep=25, crit_damage=55),
                Stat(pdamage_indep=25, crit_damage=68),
                Stat(pdamage_indep=25, crit_damage=82),
                Stat(pdamage_indep=25, crit_damage=96),
                Stat(pdamage_indep=25, crit_damage=110),
            ],
        ),
    ],
)

VoidStrike = SkillSpecification(
    name="보이드 스트라이크",
    damage_table={
        10: (3561, 19.306),
        11: (3563, 21.003),
        12: (3564, 22.048),
    },
    back=True,
    tripods=[
        Tripod(
            name="암흑 공격",
            stat_list=[
                Stat(pdamage_indep=30),
                Stat(pdamage_indep=37),
                Stat(pdamage_indep=44),
                Stat(pdamage_indep=52),
                Stat(pdamage_indep=60),
            ],
        ),
    ],
)

VoidStrikeExplosion = SkillSpecification(
    name="보이드 스트라이크(블랙 익스플로젼)",
    damage_table={
        10: (3561, 19.306),
        11: (3563, 21.003),
        12: (3564, 22.048),
    },
    tripods=[
        Tripod(
            name="암흑 공격",
            stat_list=[
                Stat(pdamage_indep=30),
                Stat(pdamage_indep=37),
                Stat(pdamage_indep=44),
                Stat(pdamage_indep=52),
                Stat(pdamage_indep=60),
            ],
        ),
        Tripod(
            name="블랙 익스플로젼",
            stat_list=[
                Stat(pdamage_indep=70 - 100),
                Stat(pdamage_indep=78.4 - 100),
                Stat(pdamage_indep=86.8 - 100),
                Stat(pdamage_indep=95.9 - 100),
                Stat(pdamage_indep=105.0 - 199),
            ],
        ),
    ],
)

BladeBurst = SkillSpecification(
    name="블레이드 버스트",
    damage_table={
        11: (7244, 42.873),
    },
    back=True,
    tripods=[],
)