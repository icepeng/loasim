from loasim.core import SkillSpecification, Stat, Tripod
from loasim.core.skill import SkillRepository

lostark_scouter_skill_repository = SkillRepository()

lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="명령 : 레이드 미사일",
        type="Normal",
        damage_table={
            12: (3066, 19.10),
        },
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
)

lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="명령 : 베이비 드론",
        type="Area",
        damage_table={
            12: (3200, 19.71),
        },
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
)

lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="코멧 스트라이크",
        type="Area",
        damage_table={
            12: (1809, 11.27),
        },
    )
)
lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="슬러그 샷",
        type="Area",
        damage_table={
            12: (1841, 11.50),
        },
    )
)
lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="레이저 블레이드",
        type="Area",
        damage_table={
            12: (3707, 23.13),
        },
    )
)
lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="엑셀리온 빔",
        type="Area",
        damage_table={
            12: (4603, 28.70),
        },
        head=True,
    )
)
lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="버스트 블로우",
        type="Area",
        damage_table={
            12: (3488, 21.71),
        },
    )
)
lostark_scouter_skill_repository.add(
    SkillSpecification(
        name="크림슨 브레이커",
        type="Area",
        damage_table={
            12: (7200, 44.94),
        },
    )
)
