from dataclasses import dataclass

from .slot import Slot

@dataclass(kw_only=True)
class WorkingHour:
    week: int
    slot: Slot
