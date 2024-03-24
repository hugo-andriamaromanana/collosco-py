from typing import Type
from pandas import read_csv
from pathlib import Path

from ..data_objects.group_objects import Slot, Teacher, Subject


def _from_subject_name_get_subject(subject_name: str) -> Subject:
    for subject in Subject:
        if subject.value == subject_name:
            return subject
    raise ValueError("Failed to find subject name")


def create_teachers_schedule(path_to_teachers_csv: Path) -> list[Teacher]:
    """Returns a list of teacher with their slots filled up"""
    teachers: dict[str, Teacher] = {}
    teachers_csv = read_csv(path_to_teachers_csv, sep=";")
    for _, row in teachers_csv.iterrows():
        teacher_name = row["professeur"]
        current_slot = Slot(day=row["jour"], hours=row["heure"])
        if teacher_name not in teachers:
            teachers[teacher_name] = Teacher(
                name=row["professeur"],
                subject=_from_subject_name_get_subject(row["matiere"]),
            )
        teachers[teacher_name].slots.append(current_slot)
    return list(teachers.values())

def get_teachers_for_subjects(teachers: list[Teacher]) -> dict[Subject, list[Teacher]]:
    teachers_for_subjects = {subject:[] for subject in Subject}
    for teacher in teachers:
        teachers_for_subjects[teacher.subject].append(teacher)
    return teachers_for_subjects 