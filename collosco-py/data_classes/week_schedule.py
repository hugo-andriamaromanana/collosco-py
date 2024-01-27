from dataclasses import dataclass, field
from .trinomes import Trinomes
from .exam import Exam


@dataclass(kw_only=True)
class WeekSchedule:
    id: int
    groups_included: list[Trinomes] = field(default_factory=list)
    exam_dates: list[Exam] = field(default_factory=list)
