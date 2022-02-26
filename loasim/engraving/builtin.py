from loasim.core import StaticBuff, StackBuff, SkillBuff, Stat, Skill
from loasim.engraving.base import Engraving, EngravingRepository

lostark_engraving_repository = EngravingRepository()

lostark_engraving_repository.add(
    Engraving(
        name="원한",
        buff_list=[
            StaticBuff(
                stat=Stat(pdamage_indep=4),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=10),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=20),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="예리한 둔기",
        buff_list=[
            StaticBuff(
                stat=Stat(pdamage_indep=-2, crit_damage=10),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=-2, crit_damage=25),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=-2, crit_damage=50),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="저주받은 인형",
        buff_list=[
            StaticBuff(
                stat=Stat(patt_common=3),
            ),
            StaticBuff(
                stat=Stat(patt_common=8),
            ),
            StaticBuff(
                stat=Stat(patt_common=16),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="정밀 단도",
        buff_list=[
            StaticBuff(
                stat=Stat(crit=4, crit_damage=-12),
            ),
            StaticBuff(
                stat=Stat(crit=10, crit_damage=-12),
            ),
            StaticBuff(
                stat=Stat(crit=20, crit_damage=-12),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="바리케이드",
        buff_list=[
            StaticBuff(
                stat=Stat(pdamage_indep=3),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=8),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=16),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="안정된 상태",
        buff_list=[
            StaticBuff(
                stat=Stat(pdamage_indep=3),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=8),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep=16),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="아드레날린",
        buff_list=[
            StaticBuff(
                stat=Stat(patt_common=1.8, crit=5),
            ),
            StaticBuff(
                stat=Stat(patt_common=3.6, crit=10),
            ),
            StaticBuff(
                stat=Stat(patt_common=6, crit=15),
            ),
        ],
    )
)


def is_hit_master(skill: Skill):
    return not (skill.head or skill.back)


lostark_engraving_repository.add(
    Engraving(
        name="타격의 대가",
        buff_list=[
            SkillBuff(
                get_stat=lambda skill: Stat(pdamage_indep=is_hit_master(skill) * 3),
            ),
            SkillBuff(
                get_stat=lambda skill: Stat(pdamage_indep=is_hit_master(skill) * 8),
            ),
            SkillBuff(
                get_stat=lambda skill: Stat(pdamage_indep=is_hit_master(skill) * 16),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="기습의 대가",
        buff_list=[
            StaticBuff(
                stat=Stat(pdamage_indep_back=5),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep_back=12),
            ),
            StaticBuff(
                stat=Stat(pdamage_indep_back=25),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="돌격대장",
        buff_list=[
            StackBuff(
                get_stat=lambda stack: Stat(pdamage_indep=min(stack, 40) * 0.1),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(pdamage_indep=min(stack, 40) * 0.22),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(pdamage_indep=min(stack, 40) * 0.45),
            ),
        ],
    )
)


def is_super_charge(skill: Skill):
    return skill.type == "Charge"


lostark_engraving_repository.add(
    Engraving(
        name="슈퍼 차지",
        buff_list=[
            SkillBuff(
                get_stat=lambda skill: Stat(pdamage_indep=is_super_charge(skill) * 4),
            ),
            SkillBuff(
                get_stat=lambda skill: Stat(pdamage_indep=is_super_charge(skill) * 10),
            ),
            SkillBuff(
                get_stat=lambda skill: Stat(pdamage_indep=is_super_charge(skill) * 20),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="진화의 유산",
        buff_list=[
            StackBuff(
                get_stat=lambda stack: Stat(pdamage_indep=stack * 2),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(pdamage_indep=stack * 4),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(pdamage_indep=stack * 6),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="회귀",
        buff_list=[
            StaticBuff(
                stat=Stat(crit=6, crit_damage=20),
            ),
            StaticBuff(
                stat=Stat(crit=9, crit_damage=30),
            ),
            StaticBuff(
                stat=Stat(crit=12, crit_damage=40),
            ),
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
    Engraving(
        name="잔재된 기운",
        buff_list=[
            StackBuff(
                get_stat=lambda stack: Stat(patt_job=get_blade_buff(1, stack)),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(patt_job=get_blade_buff(2, stack)),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(patt_job=get_blade_buff(3, stack)),
            ),
        ],
    )
)

lostark_engraving_repository.add(
    Engraving(
        name="버스트",
        buff_list=[
            StackBuff(
                get_stat=lambda stack: Stat(pdamage_indep=stack * 7.5),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(
                    pdamage_indep=stack * 7.5, patt_job=stack * 0.5
                ),
            ),
            StackBuff(
                get_stat=lambda stack: Stat(
                    pdamage_indep=stack * 7.5,
                    patt_job=stack * 1,
                ),
            ),
        ],
    )
)
