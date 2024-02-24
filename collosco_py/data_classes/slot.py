from dataclasses import dataclass
from datetime import time
from typing import Tuple


@dataclass(kw_only=True)
class Slot:
    day: str
    hours: Tuple[time, time]
