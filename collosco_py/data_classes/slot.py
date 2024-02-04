from dataclasses import dataclass


@dataclass(kw_only=True)
class Slot:
    day: str
    hour: int
    