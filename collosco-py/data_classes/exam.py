from dataclasses import dataclass


@dataclass(kw_only=True)
class Exam:
    day: str
    week_id: int
    hour: float
    teacher: str
    module: str
