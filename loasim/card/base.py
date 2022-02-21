from typing import List, Optional, Tuple

from pydantic import BaseModel

from loasim.core.stat import Stat


class Card(BaseModel):
    name: str
    stat: Stat


class CardRepository:
    def __init__(self):
        self._cards = {}

    def add(self, card: Card):
        self._cards[card.name] = card

    def get(self, card_name) -> Optional[Card]:
        return self._cards.get(card_name)
