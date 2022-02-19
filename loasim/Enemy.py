class Enemy:
    def __init__(self, armor: float, reduction: float) -> None:
        self.armor = armor
        self.reduction = reduction

    def get_reduction_rate(self, armor_ignore) -> float:
        armor = self.armor * (100 - armor_ignore) / 100
        return (1 - armor / (armor + 6500)) * (1 - self.reduction / 100)
