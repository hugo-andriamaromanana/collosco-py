from dataclasses import dataclass, field
from datetime import time
from typing import Tuple

from .exam_types import Exam, Kholle, Subject

@dataclass
class Slot:
    day: str
    hours: Tuple[time, time]

@dataclass
class Student:
    group_name: str
    group_nb: int
    group_tp: str
    tag: str

@dataclass
class Teacher:
    name: str
    subject: Subject
    slots: list[Slot] = field(default_factory=list)


@dataclass
class Trinome:
    id: int
    group_td: int
    group_tp: str
    exams: list[Exam] = field(default_factory=list)
    
@dataclass
class UnavailableTime:
    week: int
    slot: Slot
    group_tag: str
    
@dataclass
class WeekSchedule:
    id: int
    # groups_included: list[Trinome] = field(default_factory=list)
    kholles_dates: list[Kholle] = field(default_factory=list)
    
@dataclass
class WorkingHour:
    week: int
    slot: Slot