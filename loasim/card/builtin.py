from pydantic import BaseModel
from typing import Optional, List
from loasim.core.stat import Stat
from loasim.card.base import Card, CardRepository


lostark_default_card_repository = CardRepository()

lostark_default_card_repository.add(
    Card(name="남겨진 바람의 절벽 (12)", stat=Stat(crit=7))
)
lostark_default_card_repository.add(
    Card(name="세상을 구하는 빛 (18)", stat=Stat(pdamage_indep=7)),
)
lostark_default_card_repository.add(
    Card(name="세상을 구하는 빛 (30)", stat=Stat(pdamage_indep=15)),
)
