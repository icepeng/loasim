from loasim.core import InternalStatOnoffBuff, Stat
from loasim.job.base import Job, SkillSpecification, Tripod

lostark_job_artist = Job()

lostark_job_artist.add_buff(
    InternalStatOnoffBuff(
        name="저무는 달",
        stat_fn=lambda internal_stat: Stat(
            pdamage_indep=10 * (1 + internal_stat.special * 0.000543611)
        ),
    )
)

lostark_job_artist.add_skill(
    SkillSpecification(
        name="필법 : 한획긋기",
        type="Normal",
        damage_table={
            11: (5978, 19.13),
        },
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
                type_override="Charge",
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
)

lostark_job_artist.add_skill(
    SkillSpecification(
        name="묵법 : 두루미나래",
        type="Normal",
        damage_table={
            11: (5988, 19.16),
        },
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
                type_override="Area",
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
)

lostark_job_artist.add_skill(
    SkillSpecification(
        name="묵법 : 범가르기",
        type="Normal",
        damage_table={
            11: (5169, 16.54),
        },
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
)

lostark_job_artist.add_skill(
    SkillSpecification(
        name="묵법 : 달그리기",
        type="Casting",
        damage_table={
            11: (5070, 16.25),
        },
        tripods=[
            Tripod(
                name="별 그리기",
                type_override="Charge",
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
                type_override="Normal",
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
)

lostark_job_artist.add_skill(
    SkillSpecification(
        name="묵법 : 먹오름",
        type="Area",
        damage_table={
            11: (478, 1.55),
        },
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
)

lostark_job_artist.add_skill(
    SkillSpecification(
        name="묵법 : 해그리기",
        type="Normal",
        damage_table={
            10: (0, 0),
        },
        tripods=[
            Tripod(
                name="음의 기운 발산",
                stat_list=[
                    Stat(pdamage_indep=100),
                    Stat(pdamage_indep=111),
                    Stat(pdamage_indep=122),
                    Stat(pdamage_indep=133),
                    Stat(pdamage_indep=145),
                ],
            ),
            Tripod(
                name="나만의 권능",
                buff_stat_list=[
                    Stat(crit=35.0),
                    Stat(crit=38.5),
                    Stat(crit=42.0),
                    Stat(crit=45.9),
                    Stat(crit=49.7),
                ],
            ),
        ],
    )
)

lostark_job_artist.add_skill(
    SkillSpecification(
        name="묵법 : 해우물",
        type="Normal",
        damage_table={
            10: (0, 0),
        },
        tripods=[
            Tripod(
                name="나만의 우물",
                stat_list=[
                    Stat(pdamage_indep=20),
                    Stat(pdamage_indep=26),
                    Stat(pdamage_indep=32),
                    Stat(pdamage_indep=38),
                    Stat(pdamage_indep=45),
                ],
                buff_stat_list=[
                    Stat(patt_indep=30),
                    Stat(patt_indep=30),
                    Stat(patt_indep=30),
                    Stat(patt_indep=30),
                    Stat(patt_indep=30),
                ],
            ),
        ],
    )
)
