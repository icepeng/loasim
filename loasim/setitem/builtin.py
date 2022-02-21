from loasim.setitem.base import SetItemRepository, SetItem, SetItemState
from loasim.core import Stat


lostark_setitem_repository = SetItemRepository()


lostark_setitem_repository.add(
    SetItem(
        "환각",
        [
            (Stat(), Stat()),  #  2환각 미지원
            (Stat(crit=15), Stat(crit=18)),
            (Stat(pdamage_indep=25, crit=5), Stat(pdamage_indep=29, crit=7)),
        ],
    )
)

lostark_setitem_repository.add(
    SetItem(
        "악몽",
        [
            (Stat(pdamage_indep=12), Stat(pdamage_indep=15)),
            (Stat(pdamage=15), Stat(pdamage=18)),
            (Stat(pdamage_indep=15), Stat(pdamage_indep=18)),
        ],
    ),
)

lostark_setitem_repository.add(
    SetItem(
        "지배",
        [
            (Stat(pdamage_indep=10), Stat(pdamage_indep=10)),
            (
                Stat(pdamage_indep=25)
                - Stat(pdamage_indep=10),
                Stat(pdamage_indep=28)
                - Stat(pdamage_indep=10),
            ),
            (Stat(pdamage_indep=15), Stat(pdamage_indep=18)),
        ],
    )
)

lostark_setitem_repository.add(
    SetItem(
        "구원",
        [
            (Stat(pdamage=14), Stat(pdamage=18)),
            (Stat(pdamage=14), Stat(pdamage=18)),
            (
                Stat(pdamage=14, pdamage_indep=5),
                Stat(pdamage=18, pdamage_indep=5),
            ),
        ],
    ),
)
