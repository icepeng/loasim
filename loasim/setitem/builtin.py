from loasim.core import OnoffBuff, SkillBuff, StackBuff, Stat
from loasim.core.stat import sub_pdamage_indep
from loasim.setitem.base import SetItem, SetItemRepository

lostark_setitem_repository = SetItemRepository()


lostark_setitem_repository.add(
    SetItem(
        name="환각",
        stat_list=[
            None,
            (
                Stat(crit=15),
                Stat(crit=18),
            ),
            None,
        ],
        buff_list=[
            (
                OnoffBuff(name="환각", stat=Stat(pdamage_indep=13)),
                OnoffBuff(name="환각", stat=Stat(pdamage_indep=15)),
            ),
            None,
            (
                OnoffBuff(name="실체", stat=Stat(pdamage_indep=25, crit=5)),
                OnoffBuff(name="실체", stat=Stat(pdamage_indep=29, crit=7)),
            ),
        ],
    )
)

lostark_setitem_repository.add(
    SetItem(
        name="악몽",
        stat_list=[
            None,
            None,
            None,
        ],
        buff_list=[
            (
                SkillBuff(
                    name="악몽",
                    stat_fn=lambda skill: Stat(pdamage_indep=skill.consume_mana * 12),
                ),
                SkillBuff(
                    name="악몽",
                    stat_fn=lambda skill: Stat(pdamage_indep=skill.consume_mana * 15),
                ),
            ),
            (
                OnoffBuff(
                    name="마나 중독",
                    stat=Stat(pdamage=15),
                ),
                OnoffBuff(
                    name="마나 중독",
                    stat=Stat(pdamage=18),
                ),
            ),
            (
                OnoffBuff(
                    name="마나 중독",
                    stat=Stat(pdamage_indep=15),
                ),
                OnoffBuff(
                    name="마나 중독",
                    stat=Stat(pdamage_indep=18),
                ),
            ),
        ],
    ),
)

lostark_setitem_repository.add(
    SetItem(
        name="지배",
        stat_list=[
            None,
            None,
            None,
        ],
        buff_list=[
            (
                OnoffBuff(
                    name="내면의 각성",
                    stat=Stat(pdamage_indep=10),
                ),
                OnoffBuff(
                    name="내면의 각성",
                    stat=Stat(pdamage_indep=10),
                ),
            ),
            (
                OnoffBuff(
                    name="내면의 각성",
                    stat=Stat(pdamage_indep=25) - Stat(pdamage_indep=10),
                ),
                OnoffBuff(
                    name="내면의 각성",
                    stat=Stat(pdamage_indep=28) - Stat(pdamage_indep=10),
                ),
            ),
            (
                OnoffBuff(
                    name="내면의 각성",
                    stat=Stat(pdamage_indep=15),
                ),
                OnoffBuff(
                    name="내면의 각성",
                    stat=Stat(pdamage_indep=18),
                ),
            ),
        ],
    )
)

lostark_setitem_repository.add(
    SetItem(
        name="구원",
        stat_list=[
            None,
            None,
            None,
        ],
        buff_list=[
            (
                StackBuff(
                    name="고양",
                    stat_fn=lambda stack: Stat(pdamage=min(stack, 20) * 0.7),
                ),
                StackBuff(
                    name="고양",
                    stat_fn=lambda stack: Stat(pdamage=min(stack, 20) * 0.9),
                ),
            ),
            (
                StackBuff(
                    name="고양",
                    stat_fn=lambda stack: Stat(pdamage=min(stack, 20) * 0.7),
                ),
                StackBuff(
                    name="고양",
                    stat_fn=lambda stack: Stat(pdamage=min(stack, 20) * 0.9),
                ),
            ),
            (
                StackBuff(
                    name="고양",
                    stat_fn=lambda stack: Stat(
                        pdamage=min(stack, 20) * 0.7, pdamage_indep=(stack == 20) * 5
                    ),
                ),
                StackBuff(
                    name="고양",
                    stat_fn=lambda stack: Stat(
                        pdamage=min(stack, 20) * 0.9, pdamage_indep=(stack == 20) * 5
                    ),
                ),
            ),
        ],
    ),
)

lostark_setitem_repository.add(
    SetItem(
        name="사멸",
        stat_list=[
            (
                Stat(crit_damage=17, crit_damage_back=55 - 17),
                Stat(crit_damage=20, crit_damage_back=60 - 20),
            ),
            (
                Stat(crit=17),
                Stat(crit=20),
            ),
            (
                Stat(
                    pdamage_indep=7,
                    pdamage_indep_back=sub_pdamage_indep(21, 7),
                ),
                Stat(
                    pdamage_indep=8,
                    pdamage_indep_back=sub_pdamage_indep(24, 8),
                ),
            ),
        ],
        buff_list=[None, None, None],
    ),
)
