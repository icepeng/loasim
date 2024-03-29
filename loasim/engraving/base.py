from typing import Callable, Dict, List

from pydantic import BaseModel

from loasim.core import (
    AbstractBuff,
    OnoffBuff,
    Skill,
    SkillBuff,
    StackBuff,
    Stat,
    StatBuff,
    StaticBuff,
)


class AbstractEngraving(BaseModel):
    name: str

    def get_buff(self, level: int) -> AbstractBuff:
        raise NotImplementedError()


class OnoffEngraving(AbstractEngraving):
    stat_list: List[Stat]

    def get_buff(self, level: int) -> OnoffBuff:
        return OnoffBuff(
            name=self.name,
            stat=self.stat_list[level - 1],
        )


class StaticEngraving(AbstractEngraving):
    stat_list: List[Stat]

    def get_buff(self, level: int) -> StaticBuff:
        return StaticBuff(
            name=self.name,
            stat=self.stat_list[level - 1],
        )


class StackEngraving(AbstractEngraving):
    stat_fn_list: List[Callable[[int], Stat]]

    def get_buff(self, level: int) -> StackBuff:
        return StackBuff(
            name=self.name,
            stat_fn=self.stat_fn_list[level - 1],
        )


class SkillEngraving(AbstractEngraving):
    stat_fn_list: List[Callable[[Skill], Stat]]

    def get_buff(self, level: int) -> SkillBuff:
        return SkillBuff(
            name=self.name,
            stat_fn=self.stat_fn_list[level - 1],
        )


class StatEngraving(AbstractEngraving):
    stat_fn_list: List[Callable[[Stat], Stat]]

    def get_buff(self, level: int) -> StatBuff:
        return StatBuff(
            name=self.name,
            stat_fn=self.stat_fn_list[level - 1],
        )


class EngravingRepository:
    def __init__(self):
        self._engravings: Dict[str, AbstractEngraving] = {}

    def add(self, engraving: AbstractEngraving):
        self._engravings[engraving.name] = engraving

    def get_buffs(self, engraving_status: Dict[str, int]) -> List[AbstractBuff]:
        buffs: List[AbstractBuff] = []
        for name, level in engraving_status.items():
            engraving = self._engravings.get(name)
            if engraving is None:
                raise Exception(f"{name} is not an engraving")
            buffs.append(engraving.get_buff(level))

        return buffs
