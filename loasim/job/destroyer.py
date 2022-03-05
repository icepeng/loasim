from typing import Dict

from loasim.core.buff import AbstractBuff, BuffState, OnoffBuff
from loasim.core.skill import Skill
from loasim.core.stat import InternalStat, Stat
from loasim.job.base import Job, SkillSpecification, Tripod

lostark_job_destroyer = Job()


class GravityCoreBuff(AbstractBuff):
    name: str

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ):
        buff_state = state.get(self.name)
        if buff_state is None:
            raise ValueError(f"{self.name} is not found in state")
        if not buff_state.onoff:
            return Stat()

        core = buff_state.stack
        if core == 3:
            core_bonus = 45
        elif core == 2:
            core_bonus = 20
        elif core == 1:
            core_bonus = 10
        else:
            core_bonus = 0

        special = internal_stat.special
        core_damage = (1 + special * 0.00082255) * core_bonus

        return Stat(pdamage_indep=core_damage)


lostark_job_destroyer.add_buff(GravityCoreBuff(name="중력 코어"))

lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="헤비 크러쉬",
        type="Normal",
        head=True,
        damage_table={
            12: (840, 4.47),
        },
        tripods=[
            Tripod(
                name="순간타격",
                stat_list=[],
            ),
            Tripod(
                name="행운의 코어",
                stat_list=[],
            ),
        ],
    )
)

lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="인듀어 페인",
        type="Normal",
        head=True,
        back=True,
        damage_table={
            10: (1939, 9.05),
        },
        tripods=[
            Tripod(
                name="넓은 타격",
                stat_list=[],
            ),
            Tripod(
                name="고통의 흔적",
                buff_stat_list=[Stat(armor_ignore=24)],
            ),
            Tripod(
                name="건강한 정신",
                stat_list=[],
            ),
        ],
    )
)

lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="그라비티 임팩트",
        type="Normal",
        damage_table={
            10: (1224, 5.97),
        },
        tripods=[
            Tripod(
                name="행운의 코어",
                stat_list=[],
            ),
            Tripod(
                name="단단한 정신",
                stat_list=[],
            ),
            Tripod(
                name="의지 강화",
                stat_list=[],
            ),
        ],
    )
)
lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="드레드노트",
        type="Normal",
        head=True,
        damage_table={
            11: (492, 5.69),
        },
        tripods=[
            Tripod(
                name="강인함",
                stat_list=[],
            ),
            Tripod(
                name="단단한 신체",
                stat_list=[],
            ),
            Tripod(
                name="몰아치는 해머",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=60)],
            ),
        ],
    )
)
lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="러닝 크래쉬",
        type="Holding",
        head=True,
        damage_table={
            7: (1847, 9.56),
        },
        tripods=[
            Tripod(
                name="행운의 코어",
                stat_list=[],
            ),
            Tripod(
                name="집중 표적",
                stat_list=[],
            ),
        ],
    )
)
lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="퍼펙트 스윙",
        type="Charge",
        head=True,
        back=True,
        damage_table={
            12: (3849, 20.54),
        },
        tripods=[
            Tripod(
                name="약점포착",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=45)],
            ),
            Tripod(
                name="날카로운 해머",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=71)],
            ),
            Tripod(
                name="무절제",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=145)],
            ),
        ],
    )
)
lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="사이즈믹 해머",
        type="Normal",
        head=True,
        back=True,
        damage_table={
            12: (3573, 19.07),
        },
        tripods=[
            Tripod(
                name="절대적인 힘",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=60)],
            ),
            Tripod(
                name="날카로운 벽",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=95)],
            ),
            Tripod(
                name="굶주린 힘",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=95.2)],
            ),
        ],
    )
)
lostark_job_destroyer.add_skill(
    SkillSpecification(
        name="풀 스윙",
        type="Charge",
        head=True,
        damage_table={
            12: (3803, 15.02),
        },
        tripods=[
            Tripod(
                name="빠른 준비",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat()],
            ),
            Tripod(
                name="무서운 해머",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=51)],
            ),
            Tripod(
                name="야수의 눈",
                stat_list=[Stat(), Stat(), Stat(), Stat(), Stat(pdamage_indep=174.5)],
            ),
        ],
    )
)
