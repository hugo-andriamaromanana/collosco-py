from dataclasses import dataclass, field
from .working_hour import WorkingHour


@dataclass(kw_only=True)
class Trinomes:
    id: int
    group_nb: int
    group_tp: str
    working_hours: list[WorkingHour] = field(default_factory=list)
