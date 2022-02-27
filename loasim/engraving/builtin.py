from loasim.core import Skill, Stat
from loasim.engraving.base import (
    EngravingRepository,
    SkillEngraving,
    StackEngraving,
    StatEngraving,
    StaticEngraving,
)

lostark_engraving_repository = EngravingRepository()

lostark_engraving_repository.add(
    StaticEngraving(
        name="원한",
        stat_list=[
            Stat(pdamage_indep=4),
            Stat(pdamage_indep=10),
            Stat(pdamage_indep=20),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="예리한 둔기",
        stat_list=[
            Stat(pdamage_indep=-2, crit_damage=10),
            Stat(pdamage_indep=-2, crit_damage=25),
            Stat(pdamage_indep=-2, crit_damage=50),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="저주받은 인형",
        stat_list=[
            Stat(patt_common=3),
            Stat(patt_common=8),
            Stat(patt_common=16),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="정밀 단도",
        stat_list=[
            Stat(crit=4, crit_damage=-12),
            Stat(crit=10, crit_damage=-12),
            Stat(crit=20, crit_damage=-12),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="바리케이드",
        stat_list=[
            Stat(pdamage_indep=3),
            Stat(pdamage_indep=8),
            Stat(pdamage_indep=16),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="안정된 상태",
        stat_list=[
            Stat(pdamage_indep=3),
            Stat(pdamage_indep=8),
            Stat(pdamage_indep=16),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="아드레날린",
        stat_list=[
            Stat(patt_common=1.8, crit=5),
            Stat(patt_common=3.6, crit=10),
            Stat(patt_common=6, crit=15),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="정기 흡수",
        stat_list=[
            Stat(moving_speed=3),
            Stat(moving_speed=8),
            Stat(moving_speed=15),
        ],
    )
)


def is_hit_master(skill: Skill):
    return not (skill.head or skill.back)


lostark_engraving_repository.add(
    SkillEngraving(
        name="타격의 대가",
        stat_fn_list=[
            lambda skill: Stat(pdamage_indep=is_hit_master(skill) * 3),
            lambda skill: Stat(pdamage_indep=is_hit_master(skill) * 8),
            lambda skill: Stat(pdamage_indep=is_hit_master(skill) * 16),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="기습의 대가",
        stat_list=[
            Stat(pdamage_indep_back=5),
            Stat(pdamage_indep_back=12),
            Stat(pdamage_indep_back=25),
        ],
    )
)

lostark_engraving_repository.add(
    StatEngraving(
        name="돌격대장",
        stat_fn_list=[
            lambda stat: Stat(pdamage_indep=min(stat.moving_speed, 40) * 0.1),
            lambda stat: Stat(pdamage_indep=min(stat.moving_speed, 40) * 0.22),
            lambda stat: Stat(pdamage_indep=min(stat.moving_speed, 40) * 0.45),
        ],
    )
)


def is_super_charge(skill: Skill):
    return skill.type == "Charge"


lostark_engraving_repository.add(
    SkillEngraving(
        name="슈퍼 차지",
        stat_fn_list=[
            lambda skill: Stat(pdamage_indep=is_super_charge(skill) * 4),
            lambda skill: Stat(pdamage_indep=is_super_charge(skill) * 10),
            lambda skill: Stat(pdamage_indep=is_super_charge(skill) * 20),
        ],
    )
)

lostark_engraving_repository.add(
    StackEngraving(
        name="진화의 유산",
        stat_fn_list=[
            lambda stack: Stat(pdamage_indep=stack * 2),
            lambda stack: Stat(pdamage_indep=stack * 4),
            lambda stack: Stat(pdamage_indep=stack * 6),
        ],
    )
)

lostark_engraving_repository.add(
    StaticEngraving(
        name="회귀",
        stat_list=[
            Stat(crit=6, crit_damage=20),
            Stat(crit=9, crit_damage=30),
            Stat(crit=12, crit_damage=40),
        ],
    )
)


def get_blade_buff(engraving_grade: int, burst_grade: int) -> int:
    buff_table = {
        1: {
            0: 0,
            1: 8,
            2: 10,
            3: 12,
        },
        2: {
            0: 0,
            1: 16,
            2: 20,
            3: 24,
        },
        3: {
            0: 0,
            1: 25,
            2: 30,
            3: 36,
        },
    }
    return buff_table.get(engraving_grade, {}).get(burst_grade, 0)


lostark_engraving_repository.add(
    StackEngraving(
        name="잔재된 기운",
        stat_fn_list=[
            lambda stack: Stat(patt_job=get_blade_buff(1, stack)),
            lambda stack: Stat(patt_job=get_blade_buff(2, stack)),
            lambda stack: Stat(patt_job=get_blade_buff(3, stack)),
        ],
    )
)

lostark_engraving_repository.add(
    StackEngraving(
        name="버스트",
        stat_fn_list=[
            lambda stack: Stat(pdamage_indep=stack * 7.5),
            lambda stack: Stat(pdamage_indep=stack * 7.5, patt_job=stack * 0.5),
            lambda stack: Stat(
                pdamage_indep=stack * 7.5,
                patt_job=stack * 1,
            ),
        ],
    )
)
