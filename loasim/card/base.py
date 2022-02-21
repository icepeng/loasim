from typing import List, Tuple
from loasim.core.stat import Stat
from pydantic import BaseModel

class Card(BaseModel):
    name: str
    stat: Stat

