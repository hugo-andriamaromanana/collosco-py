from dataclasses import dataclass
from datetime import time
from .exam import Exam
from .student import Student
from .trinome import Trinome


@dataclass
class Kholle(Exam):
    duration: time
    teacher: str
    module: str
    assigned_to: Student | Trinome
