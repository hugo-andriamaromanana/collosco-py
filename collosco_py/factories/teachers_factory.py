from pandas import DataFrame, read_csv
from pathlib import Path
from ..data_classes import Teacher, Slot
from icecream import ic

# open csv
# for each row -> if teacher not in list Add teacher
#             -> else update teacher(Slot)


def create_teachers(path_to_teachers_csv: Path) -> dict[str,Teacher]:
    teachers: dict[str,Teacher] = {}
    teachers_csv = read_csv(path_to_teachers_csv, sep=";")
    for _, row in teachers_csv.iterrows():  # row -> Serie (0, Maths, Pr GrosZizi, 10h20)
        teacher_name = row["professeur"]  # teacher -> str"Pr GrosZizi"
        current_slot = Slot(day=row["jour"], hour=row["heure"]) 
        if teacher_name not in teachers:  # teachers -> list[Teacher]
            teachers[teacher_name] = Teacher(
                name=row["professeur"],
                subject=row["matiere"],
            )    
        teachers[teacher_name].slots.append(current_slot)
    return teachers
            # fonction Update
