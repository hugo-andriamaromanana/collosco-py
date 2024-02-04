from dataclasses import dataclass, field
from .trinome import Trinome
from .exam import Exam


@dataclass(kw_only=True)
class WeekSchedule:
    id: int
    groups_included: list[Trinome] = field(default_factory=list)
    exam_dates: list[Exam] = field(default_factory=list)
