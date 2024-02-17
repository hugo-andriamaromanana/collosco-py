from dataclasses import dataclass

from .slot import Slot

@dataclass(kw_only=True)
class UnavailableTime:
    week: int
    slot: Slot
    group_tag: str
    