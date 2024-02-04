from random import randint
from pandas import DataFrame
from ..data_classes import WorkingHour, Trinome, PraticalWork, WeekSchedule, Kholle
from ..types import TeacherScheduleType, WeekScheduleType


def place_weeks(dataframe_tp: DataFrame) -> dict[int, list]:
    week_schedule = {}
    for row in dataframe_tp:
        week_schedule[row["semaine"]] = []
    return week_schedule

def fill_one_week(week_schedule: dict[int, list | list[Kholle]], trinomes: list[Trinome], teachers_schedule: TeacherScheduleType) -> list[Kholle]:
    for trinome in trinomes:
        if trinome.id % 2 == 0:
            
        else:
            pass


        


def place_kholles_in_week_schedule(week_schedule: dict[int, None], trinomes: list[Trinome]) -> WeekScheduleType:
    flag = True
    for id in week_schedule:
        if flag:
            week_schedule[id] = fill_one_week()
        if not flag:
            week_schedule[id] = fill_one_week()
        flag = not flag
        pass
    pass


def fill_working_hours_in_trinomes(
    trinomes: list[Trinome], dataframe_tp: DataFrame
) -> list[Trinome]:
    for _, row in dataframe_tp.iterrows():
        for trinome in trinomes:
            if row["Groupe"] == trinome.group_td or row["Groupe"] == trinome.group_tp:
                trinome.working_hours.append(
                    PraticalWork(
                        end_time=row["Horaire"][1],
                        day=row["Date"],
                        week_id=row["Semaine"],
                        starting_time=row["Horaire"][0],
                    )
                )
    return trinomes


def fill_weeks_up(
    working_hours: list[WorkingHour],
    trinomes: list[Trinome],
    teachers_schedule: TeacherSchedule,
    dataframe_tp: DataFrame,
) -> WeekSchedule:
    # Eviter d'avoir plusieurs fois d'affilée le même prof. D'affilée: avoir semaine n et semaine n + 2 le même prof
    # Semaine n prof X semaine n+2 prof appartenant {prof}\{prof x}
    ALL_TEACHERS = teachers_schedule.keys()
    week_schedule = place_weeks(dataframe_tp)
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
