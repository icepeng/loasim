import os

import yaml

from loasim.core import InternalStat
from loasim.gear.base import Gear, GearRepository

lostark_gear_repository = GearRepository()


with open(os.path.join(os.path.dirname(__file__), "data.yml"), encoding="utf8") as f:
    obj = yaml.safe_load(f)
    for base_item_level, grades in obj.items():
        for grade, categories in grades.items():
            for category, internal_stats in categories.items():
                for upgrade, internal_stat in enumerate(internal_stats):
                    gear = Gear(
                        base_item_level=base_item_level,
                        grade=grade,
                        category=category,
                        upgrade=upgrade,
                        internal_stat=InternalStat.parse_obj(internal_stat),
                    )
                    lostark_gear_repository.add(gear)
