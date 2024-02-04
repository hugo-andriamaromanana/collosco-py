from dataclasses import dataclass, field
from .working_hour import WorkingHour


@dataclass(kw_only=True)
class Trinome:
    id: int
    group_td: int
    group_tp: str
    working_hours: set[WorkingHour] = field(default_factory=set)