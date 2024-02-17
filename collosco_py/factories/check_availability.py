from pandas import DataFrame

from ..data_classes.trinome import Trinome

from ..data_classes import WorkingHour, WeekSchedule, Kholle, Teacher 
from ..consts import MAXIMUM_TEACHER_PER_WEEK_OCCURENCE

def is_teacher_too_frequent(previous_weeks: list[WeekSchedule], teacher: Teacher) -> bool:
    counter = 0
    for week in previous_weeks: 
        for kholle in week.kholles_dates:
            if kholle.teacher_name == teacher.name:
                counter += 1
    return not counter == MAXIMUM_TEACHER_PER_WEEK_OCCURENCE


def is_teacher_free() -> None:
    pass


def is_group_free() -> None:
    pass


def check_if_empty(week_schedule: dict[int, list | list[Kholle]], week_id: int) -> bool:
    return week_schedule[week_id] == []


def can_place_group(
    previous_weeks: list[WeekSchedule],
    trinome: Trinome,
    week_id: int,
    teacher: Teacher
) -> bool:
    return is_teacher_free() and is_group_free() and is_teacher_too_frequent()
