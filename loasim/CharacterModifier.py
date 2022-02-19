from __future__ import annotations
from math import sqrt


class Stat:
    def __init__(
        self,
        weapon_att: float = 0,
        stat_main: float = 0,
        crit: float = 0,
        special: float = 0,
        swift: float = 0,
    ) -> None:
        self.weapon_att = weapon_att
        self.stat_main = stat_main
        self.crit = crit
        self.special = special
        self.swift = swift

    def get_mdf(self):
        return CharacterModifier(
            crit=self.crit * 0.03577,
            crit_damage=200,
            att=sqrt(self.weapon_att * self.stat_main / 6),
        )

    def get_spd(self):
        return self.swift * 0.01717


class CharacterModifier:
    def __init__(
        self,
        crit: float = 0,
        crit_damage: float = 0,
        pdamage: float = 0,
        pdamage_indep: float = 0,
        armor_ignore: float = 0,
        patt: float = 0,
        att: float = 0,
    ) -> None:
        self.crit = crit
        self.crit_damage = crit_damage

        self.pdamage = pdamage
        self.pdamage_indep = pdamage_indep

        self.armor_ignore = armor_ignore

        self.att = att
        self.patt = patt

    def __add__(self, arg: CharacterModifier) -> CharacterModifier:
        return CharacterModifier(
            crit=self.crit + arg.crit,
            crit_damage=self.crit_damage + arg.crit_damage,
            pdamage=self.pdamage + arg.pdamage,
            pdamage_indep=self.pdamage_indep
            + arg.pdamage_indep
            + (self.pdamage_indep * arg.pdamage_indep) * 0.01,
            armor_ignore=100
            - 0.01 * ((100 - self.armor_ignore) * (100 - arg.armor_ignore)),
            patt=self.patt + arg.patt,
            att=self.att + arg.att,
        )

    def add_indep(self, arg: CharacterModifier) -> CharacterModifier:
        return CharacterModifier(
            crit=self.crit + arg.crit,
            crit_damage=self.crit_damage + arg.crit_damage,
            pdamage=self.pdamage + arg.pdamage,
            pdamage_indep=self.pdamage_indep
            + arg.pdamage_indep
            + (self.pdamage_indep * arg.pdamage_indep) * 0.01,
            armor_ignore=100
            - 0.01 * ((100 - self.armor_ignore) * (100 - arg.armor_ignore)),
            patt=self.patt + arg.patt + (self.patt * arg.patt) * 0.01,
            att=self.att + arg.att,
        )

    def log(self) -> str:
        txt = "crit rate : %.1f, crit damage : %.1f\n" % (self.crit, self.crit_damage)
        txt += "pdamage : %.1f, pdamage_indep : %.1f\n" % (
            self.pdamage,
            self.pdamage_indep,
        )
        txt += "att : %.1f, patt : %.1f\n" % (self.att, self.patt)
        txt += "armor ignore : %.1f\n" % (self.armor_ignore)
        return txt

    def __repr__(self) -> str:
        return self.log()
