from pandas import DataFrame
from ..data_classes import WorkingHour, Trinome, PraticalWork, WeekSchedule, Kholle
from ..types import TeacherScheduleType, WeekScheduleType
from ..consts import TEACHER_LIMIT


def too_much_teacher(week_schedule: dict[int, list[Kholle]], week_id: int) -> bool:

    return (
        week_schedule[week_id] == week_schedule[week_id - 2]
        and week_schedule[week_id] == week_schedule[week_id - 2 * 2]...
        and week_schedule[week_id] == week_schedule[week_id - 2 * TEACHER_LIMIT]
    )


def is_teacher_free() -> bool:
    pass


def is_group_free() -> bool:
    pass


def check_if_empty(week_schedule: dict[int, list | list[Kholle]], week_id: int) -> bool:
    return week_schedule[week_id] == []


def is_group_elligible(
    workinghours: list[WorkingHour],
    teachers_schedule: TeacherScheduleType,
    week_schedule: dict[int, list | list[Kholle]],
    week_id: int,
) -> bool:
    return not (check_if_empty(week_schedule, week_id))
