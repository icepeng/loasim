from loasim.core import Stat
from loasim.core.stat import sub_pdamage_indep
from loasim.setitem.base import SetItem, SetItemRepository

lostark_setitem_repository = SetItemRepository()


lostark_setitem_repository.add(
    SetItem(
        name="환각",
        stat_list=[
            (Stat(), Stat()),  #  2환각 미지원
            (Stat(crit=15), Stat(crit=18)),
            (Stat(pdamage_indep=25, crit=5), Stat(pdamage_indep=29, crit=7)),
        ],
    )
)

lostark_setitem_repository.add(
    SetItem(
        name="악몽",
        stat_list=[
            (Stat(pdamage_indep=12), Stat(pdamage_indep=15)),
            (Stat(pdamage=15), Stat(pdamage=18)),
            (Stat(pdamage_indep=15), Stat(pdamage_indep=18)),
        ],
    ),
)

lostark_setitem_repository.add(
    SetItem(
        name="지배",
        stat_list=[
            (Stat(pdamage_indep=10), Stat(pdamage_indep=10)),
            (
                Stat(pdamage_indep=25) - Stat(pdamage_indep=10),
                Stat(pdamage_indep=28) - Stat(pdamage_indep=10),
            ),
            (Stat(pdamage_indep=15), Stat(pdamage_indep=18)),
        ],
    )
)

lostark_setitem_repository.add(
    SetItem(
        name="구원",
        stat_list=[
            (Stat(pdamage=14), Stat(pdamage=18)),
            (Stat(pdamage=14), Stat(pdamage=18)),
            (
                Stat(pdamage=14, pdamage_indep=5),
                Stat(pdamage=18, pdamage_indep=5),
            ),
        ],
    ),
)

lostark_setitem_repository.add(
    SetItem(
        name="사멸",
        stat_list=[
            (
                Stat(crit_damage=17, crit_damage_head=55-17,crit_damage_back=55 - 17),
                Stat(crit_damage=20, crit_damage_head=60-20,crit_damage_back=60 - 20),
            ),
            (Stat(crit=17), Stat(crit=20)),
            (
                Stat(
                    pdamage_indep=7,
                    pdamage_indep_head=sub_pdamage_indep(21, 7),
                    pdamage_indep_back=sub_pdamage_indep(21, 7),
                ),
                Stat(
                    pdamage_indep=8,
                    pdamage_indep_head=sub_pdamage_indep(24, 8),
                    pdamage_indep_back=sub_pdamage_indep(24, 8),
                ),
            ),
        ],
    ),
)
