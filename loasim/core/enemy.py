from pydantic import BaseModel


class Enemy(BaseModel):
    armor: float
    reduction: float

    def get_reduction_rate(self, armor_ignore: float) -> float:
        armor = self.armor * (100 - armor_ignore) / 100
        return (1 - armor / (armor + 6500)) * (1 - self.reduction / 100)
