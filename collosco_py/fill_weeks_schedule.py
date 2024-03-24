from random import choice
from pandas import DataFrame

from .factories.check_availability import can_place_group
from .data_objects.exam_types import Exam, Kholle
from .data_objects.group_objects import Slot, Subject, Teacher, Trinome, WeekSchedule
from .factories.extract_schedule import extract_scheduled_tp

MATHS_LV1 = [Subject.Maths, Subject.Lv1]
PHYSIQUE_CHIMIE_SII = [Subject.PhysiqueChimie, Subject.Sii]


def get_all_weeks(scheduled_tp: DataFrame) -> list[int]:
    all_weeks = []
    for week_str in scheduled_tp["Semaine"].values:
        if not week_str in all_weeks:
            all_weeks.append(int(week_str))
    return all_weeks


def init_pratical_work_in_trinomes(
    trinomes: list[Trinome], scheduled_tp: DataFrame
) -> list[Trinome]:
    for _, row in scheduled_tp.iterrows():
        for trinome in trinomes:
            if row["Groupe"] == trinome.group_td or row["Groupe"] == trinome.group_tp:
                trinome.exams.append(
                    Exam(
                        week_id=row["Semaine"],
                        slot=Slot(
                            day=row["Date"],
                            hours=(row["Horaire"][0], row["Horaire"][1]),
                        ),
                    )
                )
    return trinomes

def fill_first_spot(teachers_for_subjects: dict[Subject, list[Teacher]],trinome: Trinome,first_week: WeekSchedule) -> WeekSchedule:
    first_subject = MATHS_LV1[0]
    all_teachers_for_subject = teachers_for_subjects[first_subject]
    random_first_chosen_teacher = choice(all_teachers_for_subject)
    random_slot_from_teacher = choice(random_first_chosen_teacher.slots)
    first_kholle = Kholle(first_week.id, random_slot_from_teacher, random_first_chosen_teacher.name, first_subject)
    if can_place_group([], trinome, first_kholle):
        first_week.kholles_dates.append(first_kholle)
    return first_week


def fill_first_week(
    trinomes: list[Trinome],
    teachers: list[Teacher],
    teachers_for_subjects: dict[Subject, list[Teacher]],
    week_id: int,
) -> WeekSchedule:
    first_week = WeekSchedule(week_id)
    for trinome in trinomes:
        if trinome.id % 2 == 0:
            first_subject = MATHS_LV1[0]
            all_teachers_for_subject = teachers_for_subjects[first_subject]
            random_first_chosen_teacher = choice(all_teachers_for_subject)
            random_slot_from_teacher = choice(random_first_chosen_teacher.slots)
            first_kholle = Kholle(week_id, random_slot_from_teacher, random_first_chosen_teacher.name, first_subject)
            if can_place_group([], trinome, first_kholle):
                first_week.kholles_dates.append(first_kholle)
            else:


# def one_week_filler(trinomes: list[Trinome], teachers: list[Teacher], year_schedule: list[WeekSchedule] | list) -> WeekSchedule:
#     for trinome in trinomes:
#         if year_schedule == []:

#     while True:
#         pass


def fill_weeks_up(
    trinomes: list[Trinome],
    teachers: list[Teacher],
    scheduled_tp: DataFrame,
) -> list[WeekSchedule]:
    # Eviter d'avoir plusieurs fois d'affilée le même prof. D'affilée: avoir semaine n et semaine n + 2 le même prof
    # Semaine n prof X semaine n+2 prof appartenant {prof}\{prof x}

    all_weeks = get_all_weeks(scheduled_tp)
    year_schedule = []
    for week_id in all_weeks:
        year_schedule.append(one_week_filler(trinomes, teachers, year_schedule))

    # but
    # kholle = Kholle()

    # return WeekSchedule(
    #     id = 0,
    #     kholles_dates=["kholle machin"]
    # )

    while True:
        # Défilement des semaines
        # Quand toutes les semaines sont passées on arrête
        # on fait évoluer le compteur des semaines
        # Step 1 placer les semaines dans week schedule
        # Step 2 placer les kholles dans week schedule (contraintes)
        # Step 3 return
        while True:
            # Défilement des groupes
            # Quand tous les groupes sont attribués on arrête
            pass
    pass
