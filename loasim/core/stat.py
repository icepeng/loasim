from __future__ import annotations

from math import sqrt

from pydantic import BaseModel, Extra


class InternalStat(BaseModel):
    class Config:
        extra = Extra.forbid

    weapon_att: float = 0
    stat_main: float = 0
    pstat_main: float = 0
    crit: float = 0
    special: float = 0
    swift: float = 0

    def get_stat(self) -> Stat:
        return Stat(
            crit=self.crit * 0.03577,
            crit_damage=200,
            att=sqrt(
                self.weapon_att * (self.stat_main * (100 + self.pstat_main) / 100) / 6
            ),
            moving_speed=self.swift * 0.01717,
        )

    def __add__(self, arg: InternalStat) -> InternalStat:
        return InternalStat(
            weapon_att=self.weapon_att + arg.weapon_att,
            stat_main=self.stat_main + arg.stat_main,
            pstat_main=self.pstat_main + arg.pstat_main,
            crit=self.crit + arg.crit,
            special=self.special + arg.special,
            swift=self.swift + arg.swift,
        )


def add_pdamage_indep(a: float, b: float) -> float:
    return a + b + (a * b) * 0.01


def sub_pdamage_indep(a: float, b: float) -> float:
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
    patt_common: float = 0
    patt_job: float = 0
    patt_indep: float = 0
    att: float = 0
    moving_speed: float = 0

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
            patt_common=self.patt_common + arg.patt_common,
            patt_job=self.patt_job + arg.patt_job,
            patt_indep=add_pdamage_indep(self.patt_indep, arg.patt_indep),
            att=self.att + arg.att,
            moving_speed=self.moving_speed + arg.moving_speed,
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
            patt_common=self.patt_common - arg.patt_common,
            patt_job=self.patt_job - arg.patt_job,
            patt_indep=sub_pdamage_indep(self.patt_indep, arg.patt_indep),
            att=self.att - arg.att,
            moving_speed=self.moving_speed - arg.moving_speed,
        )

    def get_total_att(self) -> float:
        patt = add_pdamage_indep(
            add_pdamage_indep(self.patt_common, self.patt_job), self.patt_indep
        )
        return self.att * (1 + patt / 100)

    def get_multiplier(self) -> float:
        return (1 + self.pdamage_indep / 100) * (1 + self.pdamage / 100)
