from dataclasses import dataclass
from datetime import time
from .slot import Slot

@dataclass(kw_only=True)
class WorkingHour:
    week: int
    slot: Slot
