
# TeacherScheduleType = Dict[str, Teacher]

# def place_weeks(dataframe_tp: DataFrame) -> dict[int, list]:
#     week_schedule = {}
#     for row in dataframe_tp:
#         week_schedule[row["semaine"]] = []
#     return week_schedule


# def fill_one_week(
#     week_schedule: dict[int, list | list[Kholle]],
#     trinomes: list[Trinome],
#     teachers_schedule: TeacherScheduleType,
# ) -> list[Kholle]:
#     for trinome in trinomes:
#         if trinome.id % 2 == 0:
#             # take plot, check if plot macth conditions place if not keep on checking other plots
#             # else:
#             break




# def place_kholle_in_week_schedule(
#     week_schedule: WeekSchedule, kholle: Kholle
# ) -> WeekSchedule:
#     pass


from random import randint
from pandas import DataFrame

from typing import Dict


from .data_classes import WorkingHour, Trinome, PraticalWork, WeekSchedule, Kholle, Teacher, Slot

from .factories.extract_schedule import extract_scheduled_tp


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
                trinome.working_hours.append(
                    PraticalWork(
                        end_time=row["Horaire"][1],
                        week_id=row["Semaine"],
                        slot= Slot(day=row["Date"], hour=row["Horaire"][0]))
                )
    return trinomes




def fill_weeks_up(
    trinomes: list[Trinome],
    teachers: list[Teacher],
    scheduled_tp: DataFrame,
) -> list[WeekSchedule]:
    # Eviter d'avoir plusieurs fois d'affilée le même prof. D'affilée: avoir semaine n et semaine n + 2 le même prof
    # Semaine n prof X semaine n+2 prof appartenant {prof}\{prof x}
    
    all_weeks = get_all_weeks(scheduled_tp)
    
    #but 
    kholle = Kholle()
    
    
    
    
    return WeekSchedule(
        id = 0,
        kholles_dates=["kholle machin"]
    )
    
    
    
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
