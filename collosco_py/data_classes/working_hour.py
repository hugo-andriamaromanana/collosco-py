from dataclasses import dataclass
from datetime import time

@dataclass(kw_only=True)
class WorkingHour:
    week: int
    day: str
    time: time
