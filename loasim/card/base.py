from typing import List, Tuple
from loasim.core.stat import Stat
from pydantic import BaseModel
from typing import Optional, List

class Card(BaseModel):
    name: str
    stat: Stat


class CardRepository():
    def __init__(self):
        self._cards = {}

    def add(self, card: Card):
        self._cards[card.name] = card
    
    def get(self, card_name) -> Optional[Card]:
        return self._cards.get(card_name)
