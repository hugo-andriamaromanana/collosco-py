from dataclasses import dataclass
from datetime import time
from .student import Student
from .trinome import Trinome


@dataclass(kw_only=True)
class Exam:
    day: str
    week_id: int
    starting_time: time