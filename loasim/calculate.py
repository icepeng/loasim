from collections import defaultdict
from typing import List, Dict, Tuple

from loasim.core import Skill, Enemy


def calculate(dealcycle: List[Tuple[Skill, str]], cycle_time: float, enemy: Enemy):
    total_damage = 0.0
    damage_dict: Dict = defaultdict(float)
    for sk, backhead in dealcycle:
        damage = sk.get_damage(enemy, backhead)
        total_damage += damage
        damage_dict[sk.name] += damage

    for sk, dmg in damage_dict.items():
        print(sk, f"{dmg / total_damage *100:,.3f}%")
    print(f"total damage: {total_damage:,.0f}")
    print(f"dps: {total_damage / cycle_time:,.0f}")
