from pandas import DataFrame

from ..data_classes.trinome import Trinome

from ..data_classes import WorkingHour, WeekSchedule, Kholle, Teacher, ExamType 
from ..consts import MAXIMUM_TEACHER_PER_WEEK_OCCURENCE

def is_teacher_too_frequent(previous_weeks: list[WeekSchedule], kholle: Kholle) -> bool:
    counter = 0
    for week in previous_weeks: 
        for previous_kholle in week.kholles_dates:
            if previous_kholle.teacher_name == kholle.teacher_name:
                counter += 1
    return not counter == MAXIMUM_TEACHER_PER_WEEK_OCCURENCE


def test_slot(existing_kholle: Kholle, kholle: Kholle) -> bool:
    return existing_kholle.slot == kholle.slot and existing_kholle.teacher_name == kholle.teacher_name


def is_slot_free(week_schedule: list[Kholle], kholle: Kholle) -> bool:
    for existing_kholle in week_schedule:
        if test_slot(existing_kholle, kholle):
            return False
    return True


def test_kholle(working_hour: ExamType, kholle: Kholle) -> bool:
    if kholle.slot.day == working_hour.slot.day:
            if not(kholle.slot.hours[0] > working_hour.slot.hours[0] and kholle.slot.hours[1] >= working_hour.slot.hours[0]):
                return True
            if not(kholle.slot.hours[0] <= working_hour.slot.hours[0] and kholle.slot.hours[1] < working_hour.slot.hours[0]):
                return True
    return False
    

def is_group_free(trinome: Trinome, kholle: Kholle) -> bool:
    for working_hour in trinome.working_hours:
        if test_kholle():
            return False
    return True


def check_if_empty(weeks_schedule: dict[int, list | list[Kholle]], week_id: int) -> bool:
    return weeks_schedule[week_id] == []


def can_place_group(
    previous_weeks: list[WeekSchedule],
    trinome: Trinome,
    week_id: int,
    kholle: Kholle
) -> bool:
    return is_slot_free() and is_group_free() and is_teacher_too_frequent()
