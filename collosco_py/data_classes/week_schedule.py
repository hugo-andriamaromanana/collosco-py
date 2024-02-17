from dataclasses import dataclass, field

from .exam_types import Kholle

@dataclass(kw_only=True)
class WeekSchedule:
    id: int
    # groups_included: list[Trinome] = field(default_factory=list)
    kholles_dates: list[Kholle] = field(default_factory=list)
