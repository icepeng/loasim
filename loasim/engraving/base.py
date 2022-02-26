from typing import Dict, List, Tuple

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

    def get_buffs(self, engraving_state: List[Tuple[str, int]]) -> List[Buff]:
        buffs: List[Buff] = []
        for name, level in engraving_state:
            engraving = self._engravings.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            buffs.append(engraving.buff_list[level - 1])

        return buffs
