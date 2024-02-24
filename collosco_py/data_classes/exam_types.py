from dataclasses import dataclass
from .slot import Slot


@dataclass
class Exam:
    week_id: int
    slot: Slot


@dataclass
class Kholle(Exam):
    teacher_name: str
    module: str
