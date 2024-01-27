from dataclasses import dataclass, field


@dataclass(kw_only=True)
class WorkingHour:
    week: int
    day: str
    time: int
