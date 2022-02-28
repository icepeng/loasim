from __future__ import annotations

from typing import Callable, Dict, List, Union

from pydantic import BaseModel

from loasim.core.skill import Skill
from loasim.core.stat import InternalStat, Stat


class BuffState(BaseModel):
    onoff: bool
    stack: int = 0


class AbstractBuff(BaseModel):
    name: str

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ) -> Stat:
        raise NotImplementedError()


class OnoffBuff(AbstractBuff):
    name: str
    stat: Stat

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ):
        buff_state = state.get(self.name)
        if buff_state is None:
            raise ValueError(f"{self.name} is not found in state")
        if buff_state.onoff:
            return self.stat
        return Stat()


class StaticBuff(AbstractBuff):
    name: str
    stat: Stat

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ):
        return self.stat


class StackBuff(AbstractBuff):
    name: str
    stat_fn: Union[
        Callable[[int], Stat], Callable[[int], Stat]
    ]  # mypy #5485 workaround

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ):
        buff_state = state.get(self.name)
        if buff_state is None:
            raise ValueError(f"{self.name} is not found in state")
        if buff_state.onoff:
            return self.stat_fn(buff_state.stack)
        return Stat()


class SkillBuff(AbstractBuff):
    name: str
    stat_fn: Union[
        Callable[[Skill], Stat], Callable[[Skill], Stat]
    ]  # mypy #5485 workaround

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ):
        return self.stat_fn(skill)


class StatBuff(AbstractBuff):
    name: str
    stat_fn: Union[
        Callable[[Stat], Stat], Callable[[Stat], Stat]
    ]  # mypy #5485 workaround

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ):
        return self.stat_fn(stat)


class InternalStatOnoffBuff(AbstractBuff):
    name: str
    stat_fn: Union[
        Callable[[InternalStat], Stat], Callable[[InternalStat], Stat]
    ]  # mypy #5485 workaround

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        stat: Stat,
        internal_stat: InternalStat,
    ):
        buff_state = state.get(self.name)
        if buff_state is None:
            raise ValueError(f"{self.name} is not found in state")
        if buff_state.onoff:
            return self.stat_fn(internal_stat)
        return Stat()


class BuffManager:
    def __init__(self, buff_list: List[AbstractBuff]) -> None:
        self._buffs: Dict[str, AbstractBuff] = {}
        self._stat_buffs: Dict[str, StatBuff] = {}
        for buff in buff_list:
            if isinstance(buff, StatBuff):
                self._stat_buffs[buff.name] = buff
            else:
                self._buffs[buff.name] = buff

    def get_stat(
        self,
        state: Dict[str, BuffState],
        skill: Skill,
        basis_stat: Stat,
        internal_stat: InternalStat,
    ) -> Stat:
        stat = Stat()
        for buff in self._buffs.values():
            stat = stat + buff.get_stat(state, skill, stat, internal_stat)

        for buff in self._stat_buffs.values():
            stat = stat + buff.get_stat(state, skill, stat + basis_stat, internal_stat)

        return stat
