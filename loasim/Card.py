from typing import List, Tuple
from loasim.CharacterModifier import CharacterModifier


class Card:
    def __init__(self, name: str, mdf: CharacterModifier) -> None:
        self.name = name
        self.mdf = mdf

    def get_modifier(self):
        return self.mdf


card_list = [
    Card("남겨진 바람의 절벽 (12)", CharacterModifier(crit=7)),
    Card("세상을 구하는 빛 (18)", CharacterModifier(pdamage_indep=7)),
    Card("세상을 구하는 빛 (30)", CharacterModifier(pdamage_indep=15)),
]

card_dict = {card.name: card for card in card_list}


class CardManager:
    def __init__(self, *equipped_list: List[str]) -> None:
        self.equipped_list = equipped_list

    def get_static_modifier(self):
        mdf = CharacterModifier()
        for name in self.equipped_list:
            card = card_dict.get(name)
            if card is None:
                raise Exception(f"{name} is not an card")
            mdf = mdf + card.get_modifier()
        return mdf
