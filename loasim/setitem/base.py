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


class SetItemState(BaseModel):
    level1: int
    level2: int


class SetItemRepository:
    def __init__(self):
        self._set_items: Dict[str, SetItem] = {}

    def add(self, setitem: SetItem):
        self._set_items[setitem.name] = setitem

    def get_stat(self, setitem_status: Dict[str, SetItemState]) -> Stat:
        stat = Stat()
        for name, state in setitem_status.items():
            stat = stat + self._set_items[name].get_stat(state.level1, state.level2)

        return stat

    def get_buffs(self, setitem_status: Dict[str, SetItemState]) -> List[AbstractBuff]:
        buffs: List[AbstractBuff] = []
        for name, state in setitem_status.items():
            buffs += self._set_items[name].get_buffs(state.level1, state.level2)

        return buffs
