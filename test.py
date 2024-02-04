from icecream import ic
from collosco_py.factories.extract_schedule import extract_scheduled_tp

path_to_tp = "assets\colloscope-Feuille-1.csv"
extracted_schedule = extract_scheduled_tp(path_to_tp)

ic(extracted_schedule)
