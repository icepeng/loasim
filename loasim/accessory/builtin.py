import os

import yaml

from loasim.accessory.base import Accessory, AccessoryRepository
from loasim.core.stat import InternalStat

lostark_accessory_repository = AccessoryRepository()

with open(os.path.join(os.path.dirname(__file__), "data.yml"), encoding="utf8") as f:
    obj = yaml.safe_load(f)
    for grade, categories in obj.items():
        for category, internal_stat in categories.items():
            accessory = Accessory(
                grade=grade,
                category=category,
                internal_stat=InternalStat.parse_obj(internal_stat),
            )
            lostark_accessory_repository.add(accessory)
