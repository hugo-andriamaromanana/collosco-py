from dataclasses import dataclass, field

from .exam_types import Exam


@dataclass(kw_only=True)
class Trinome:
    id: int
    group_td: int
    group_tp: str
    working_hours: list[Exam] = field(default_factory=list)