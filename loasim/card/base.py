from typing import Dict, List

from pydantic import BaseModel

from loasim.core.stat import Stat


class Card(BaseModel):
    name: str
    stat: Stat


class CardRepository:
    def __init__(self):
        self._cards: Dict[str, Card] = {}

    def add(self, card: Card):
        self._cards[card.name] = card

    def get_stat(self, card_state: List[str]) -> Stat:
        stat = Stat()
        for card_name in card_state:
            card = self._cards.get(card_name)
            if card is None:
                raise TypeError(f"Given card name is not available. {card_name}")
            stat = stat + card.stat
        return stat
