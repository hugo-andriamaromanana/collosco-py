from dataclasses import dataclass, field
from .kholle import Kholles


@dataclass(kw_only=True)
class WeekSchedule:
    id: int
    # groups_included: list[Trinome] = field(default_factory=list)
    kholles_dates: list[Kholles] = field(default_factory=list)
