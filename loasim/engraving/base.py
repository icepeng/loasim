from typing import Dict, List

from pydantic import BaseModel

from loasim.core import Buff


class Engraving(BaseModel):
    name: str
    buff_list: List[Buff]


class EngravingRepository:
    def __init__(self):
        self._engravings: Dict[str, Engraving] = {}

    def add(self, engraving: Engraving):
        for buff in engraving.buff_list:
            buff.name = engraving.name
        self._engravings[engraving.name] = engraving

    def get_buffs(self, states: Dict[str, int]) -> List[Buff]:
        buffs: List[Buff] = []
        for name, level in states.items():
            engraving = self._engravings.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            buffs.append(engraving.buff_list[level - 1])

        return buffs
