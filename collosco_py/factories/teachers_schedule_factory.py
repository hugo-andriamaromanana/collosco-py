from pandas import read_csv
from pathlib import Path
from ..data_classes import Teacher, Slot

def create_teachers_schedule(path_to_teachers_csv: Path) -> list[Teacher]:
    """Returns a list of teacher with their slots filled up"""
    teachers: dict[str,Teacher] = {}
    teachers_csv = read_csv(path_to_teachers_csv, sep=";")
    for _, row in teachers_csv.iterrows():
        teacher_name = row["professeur"]
        current_slot = Slot(day=row["jour"], hours=row["heure"]) 
        if teacher_name not in teachers:
            teachers[teacher_name] = Teacher(
                name=row["professeur"],
                subject=row["matiere"],
            )    
        teachers[teacher_name].slots.append(current_slot)
    return list(teachers.values())
