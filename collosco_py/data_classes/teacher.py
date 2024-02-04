from dataclasses import dataclass, field
from .slot import Slot

@dataclass(kw_only=True)
class Teacher:
    name: str
    subject: str
    slots: list[Slot] = field(default_factory=list)
