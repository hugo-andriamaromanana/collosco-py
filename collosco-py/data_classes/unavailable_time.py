from dataclasses import dataclass
from datetime import time

@dataclass(kw_only=True)
class UnavailableWeek:
    week: int
    day: str
    hour: time
    group_tag: str
    