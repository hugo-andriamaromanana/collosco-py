from typing import Dict
from .data_classes import Teacher, Kholle


TeacherScheduleType = Dict[str, Teacher]
WeekScheduleType = Dict[int, list[Kholle]]
