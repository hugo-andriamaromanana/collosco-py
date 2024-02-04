from collosco_py.factories.teachers_factory import create_teachers
from icecream import ic


csv_path = "assets/EDT_teachers.csv"

teachers_list = create_teachers(csv_path)

ic(teachers_list)