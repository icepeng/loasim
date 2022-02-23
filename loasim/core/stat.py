from __future__ import annotations

from math import sqrt

from pydantic import BaseModel, Extra


class InternalStat(BaseModel):
    class Config:
        extra = Extra.forbid

    weapon_att: float = 0
    stat_main: float = 0
    crit: float = 0
    special: float = 0
    swift: float = 0

    def get_stat(self) -> Stat:
        return Stat(
            crit=self.crit * 0.03577,
            crit_damage=200,
            att=sqrt(self.weapon_att * self.stat_main / 6),
        )

    def get_spd(self) -> float:
        return self.swift * 0.01717


def add_pdamage_indep(a, b):
    return a + b + (a * b) * 0.01


def sub_pdamage_indep(a, b):
    return (100 + a) / (100 + b) * 100 - 100


class Stat(BaseModel):
    class Config:
        extra = Extra.forbid

    crit: float = 0
    crit_damage: float = 0
    crit_damage_head: float = 0
    crit_damage_back: float = 0
    pdamage: float = 0
    pdamage_indep: float = 0
    pdamage_indep_head: float = 0
    pdamage_indep_back: float = 0
    armor_ignore: float = 0
    patt: float = 0
    att: float = 0

    def __add__(self, arg: Stat) -> Stat:
        return Stat(
            crit=self.crit + arg.crit,
            crit_damage=self.crit_damage + arg.crit_damage,
            crit_damage_head=self.crit_damage_head + arg.crit_damage_head,
            crit_damage_back=self.crit_damage_back + arg.crit_damage_back,
            pdamage=self.pdamage + arg.pdamage,
            pdamage_indep=add_pdamage_indep(self.pdamage_indep, arg.pdamage_indep),
            pdamage_indep_head=add_pdamage_indep(
                self.pdamage_indep_head, arg.pdamage_indep_head
            ),
            pdamage_indep_back=add_pdamage_indep(
                self.pdamage_indep_back, arg.pdamage_indep_back
            ),
            armor_ignore=100
            - 0.01 * ((100 - self.armor_ignore) * (100 - arg.armor_ignore)),
            patt=self.patt + arg.patt,
            att=self.att + arg.att,
        )

    def add_indep(self, arg: Stat) -> Stat:
        return Stat(
            crit=self.crit + arg.crit,
            crit_damage=self.crit_damage + arg.crit_damage,
            crit_damage_head=self.crit_damage_head + arg.crit_damage_head,
            crit_damage_back=self.crit_damage_back + arg.crit_damage_back,
            pdamage=self.pdamage + arg.pdamage,
            pdamage_indep=add_pdamage_indep(self.pdamage_indep, arg.pdamage_indep),
            pdamage_indep_head=add_pdamage_indep(
                self.pdamage_indep_head, arg.pdamage_indep_head
            ),
            pdamage_indep_back=add_pdamage_indep(
                self.pdamage_indep_back, arg.pdamage_indep_back
            ),
            armor_ignore=100
            - 0.01 * ((100 - self.armor_ignore) * (100 - arg.armor_ignore)),
            patt=self.patt + arg.patt + (self.patt * arg.patt) * 0.01,
            att=self.att + arg.att,
        )

    def __sub__(self, arg: Stat) -> Stat:
        return Stat(
            crit=self.crit - arg.crit,
            crit_damage=self.crit_damage - arg.crit_damage,
            crit_damage_head=self.crit_damage_head - arg.crit_damage_head,
            crit_damage_back=self.crit_damage_back - arg.crit_damage_back,
            pdamage=self.pdamage - arg.pdamage,
            pdamage_indep=sub_pdamage_indep(self.pdamage_indep, arg.pdamage_indep),
            pdamage_indep_head=sub_pdamage_indep(
                self.pdamage_indep_head, arg.pdamage_indep_head
            ),
            pdamage_indep_back=sub_pdamage_indep(
                self.pdamage_indep_back, arg.pdamage_indep_back
            ),
            armor_ignore=100
            - 100 * (100 - self.armor_ignore) / (100 - arg.armor_ignore),
            patt=self.patt - arg.patt,
            att=self.att - arg.att,
        )
