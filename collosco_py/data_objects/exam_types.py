from dataclasses import dataclass
from enum import Enum

from .group_objects import Slot


class Subject(Enum):
    Maths = "Maths"
    Lv1 = "LV 1"
    PhysiqueChimie = "Physique-Chimie"
    Sii = "SII" 
    
@dataclass
class Exam:
    week_id: int
    slot: Slot


@dataclass
class Kholle(Exam):
    teacher_name: str
    subject: Subject