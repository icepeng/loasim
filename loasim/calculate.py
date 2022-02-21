from collections import defaultdict
from typing import List
from loasim.core import Skill


def calculate(dealcycle: List[Skill], cycle_time, enemy):
    total_damage = 0
    damage_dict = defaultdict(float)
    for sk in dealcycle:
        damage = sk.get_damage(enemy)
        total_damage += damage
        damage_dict[sk.name] += damage

    for sk, dmg in damage_dict.items():
        print(sk, f"{dmg / total_damage *100:,.3f}%")
    print(f"total damage: {total_damage:,.0f}")
    print(f"dps: {total_damage / cycle_time:,.0f}")
