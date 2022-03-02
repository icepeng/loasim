from typing import Dict, List, Optional, Tuple

from pydantic import BaseModel

from loasim.core.buff import AbstractBuff
from loasim.core.stat import Stat


class SetItem(BaseModel):
    name: str
    stat_list: List[Optional[Tuple[Stat, Stat]]]
    buff_list: List[Optional[Tuple[AbstractBuff, AbstractBuff]]]

    def get_stat(self, level1_set: int, level2_set: int) -> Stat:
        stat = Stat()
        for i in range(level2_set // 2):
            stat_tuple = self.stat_list[i]
            if stat_tuple is not None:
                stat = stat + stat_tuple[1]
        for i in range(level2_set // 2, level1_set // 2):
            stat_tuple = self.stat_list[i]
            if stat_tuple is not None:
                stat = stat + stat_tuple[0]
        return stat

    def get_buffs(self, level1_set: int, level2_set: int) -> List[AbstractBuff]:
        buffs: List[AbstractBuff] = []
        for i in range(level2_set // 2):
            buff_tuple = self.buff_list[i]
            if buff_tuple is not None:
                buffs.append(buff_tuple[1])
        for i in range(level2_set // 2, level1_set // 2):
            buff_tuple = self.buff_list[i]
            if buff_tuple is not None:
                buffs.append(buff_tuple[0])
        return buffs


class SetItemRepository:
    def __init__(self):
        self._set_items: Dict[str, SetItem] = {}

    def add(self, setitem: SetItem):
        self._set_items[setitem.name] = setitem

    def get_stat(self, setitem_state: List[Tuple[str, int, int]]) -> Stat:
        stat = Stat()
        for name, level1, level2 in setitem_state:
            stat = stat + self._set_items[name].get_stat(level1, level2)

        return stat

    def get_buffs(
        self, setitem_state: List[Tuple[str, int, int]]
    ) -> List[AbstractBuff]:
        buffs: List[AbstractBuff] = []
        for name, level1, level2 in setitem_state:
            buffs += self._set_items[name].get_buffs(level1, level2)

        return buffs
