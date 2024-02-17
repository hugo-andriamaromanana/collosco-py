from dataclasses import dataclass
from datetime import time


@dataclass(kw_only=True)
class Slot:
    day: str
    hour: time
