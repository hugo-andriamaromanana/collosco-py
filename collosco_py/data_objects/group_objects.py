from dataclasses import dataclass, field
from datetime import time


@dataclass(kw_only=True)
class Slot:
    day: str
    hour: time

@dataclass(kw_only=True)
class Student:
    group_name: str
    group_nb: int
    group_tp: str
    tag: str

@dataclass(kw_only=True)
class Teacher:
    name: str
    subject: str
    slots: list[Slot] = field(default_factory=list)
    
@dataclass(kw_only=True)
class Trinome:
    id: int
    group_td: int
    group_tp: str
    working_hours: list[PraticalWork | Kholle] = field(default_factory=list)

@dataclass(kw_only=True)
class UnavailableTime:
    week: int
    slot: Slot
    group_tag: str


@dataclass(kw_only=True)
class WeekSchedule:
    id: int
    # groups_included: list[Trinome] = field(default_factory=list)
    kholles_dates: list[Kholle] = field(default_factory=list)

@dataclass(kw_only=True)
class WorkingHour:
    week: int
    slot: Slot
