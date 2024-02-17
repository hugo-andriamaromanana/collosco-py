from abc import ABC
from dataclasses import dataclass
from datetime import time

from .slot import Slot

from .trinome import Trinome
from .student import Student

@dataclass(kw_only=True)
class ExamType(ABC):
    week_id: int
    slot: Slot
    

@dataclass
class Kholle(ExamType):
    duration: time
    teacher_name: str
    module: str
    assigned_to: Student | Trinome
    
@dataclass
class PraticalWork(ExamType):
    end_time: time
