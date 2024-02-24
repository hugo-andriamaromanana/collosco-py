from ..data_classes.trinome import Trinome

from ..data_classes import WeekSchedule, Kholle, Exam

MAXIMUM_TEACHER_PER_WEEK_OCCURENCE = 2


def is_teacher_too_frequent(previous_weeks: list[WeekSchedule], kholle: Kholle) -> bool:
    counter = 0
    for week in previous_weeks:
        for previous_kholle in week.kholles_dates:
            if previous_kholle.teacher_name == kholle.teacher_name:
                counter += 1
    return counter != MAXIMUM_TEACHER_PER_WEEK_OCCURENCE


def is_slot_free(week_schedule: WeekSchedule, kholle: Kholle) -> bool:
    for existing_kholle in week_schedule.kholles_dates:
        same_teacher = (existing_kholle.slot == kholle.slot) and (
            existing_kholle.teacher_name == kholle.teacher_name
        )
        if same_teacher:
            return False
    return True


def times_are_incompatible(exam: Exam, kholle: Kholle) -> bool:
    if kholle.slot.day == exam.slot.day:
        is_kholle_before_exam = (
            kholle.slot.hours[0] > exam.slot.hours[0]
            and kholle.slot.hours[1] >= exam.slot.hours[0]
        )
        is_kholle_after_exam = (
            kholle.slot.hours[0] <= exam.slot.hours[0]
            and kholle.slot.hours[1] < exam.slot.hours[0]
        )
        return not (is_kholle_before_exam or is_kholle_after_exam)
    return False


def is_group_free(trinome: Trinome, kholle: Kholle) -> bool:
    for exam in trinome.working_hours:
        if times_are_incompatible(exam, kholle):
            return False
    return True


def can_place_group(
    previous_weeks: list[WeekSchedule], trinome: Trinome, kholle: Kholle
) -> bool:
    if is_group_free(trinome, kholle) and is_teacher_too_frequent(
        previous_weeks, kholle
    ):
        return True

    return is_slot_free(previous_weeks[0], kholle)
