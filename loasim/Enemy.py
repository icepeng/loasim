class Enemy:
    def __init__(self, armor: float, reduction: float) -> None:
        self.armor = armor
        self.reduction = reduction

    def get_reduction_rate(self) -> float:
        return (1 - self.armor / (self.armor + 6500)) * (1 - self.reduction / 100)
