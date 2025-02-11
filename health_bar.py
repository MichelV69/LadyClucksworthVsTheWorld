# ------------ imports ------------
from ansi_out import * 

# ------------ class setup ------------
class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"

    def __init__(self,
                 entity,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = ANSI.colors.get(color) or ANSI.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}")
        print(f"{self.barrier}"
              f"{ANSI.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{ANSI.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
#----- end of file -----
