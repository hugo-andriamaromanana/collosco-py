from dataclasses import dataclass
from datetime import time
from .exam import Exam


@dataclass
class PraticalWork(Exam):
    end_time: time
