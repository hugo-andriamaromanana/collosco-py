import pandas as pd
from dataclasses import dataclass, field
from collections import Counter
from ast import literal_eval
import datetime
import re








@dataclass
class Exam:
    day: str
    week_id: int
    hour: float
    teacher: str
    module: str


@dataclass
class WorkingHour:
    week: int
    day: str
    time: int


@dataclass
class Trinomes:
    id: int
    group_nb: int
    group_tp: str
    working_hours: list[WorkingHour] = field(default_factory=list)


@dataclass
class WeekSchedule:
    id: int
    groups_included: list[Trinomes] = field(default_factory=list)
    exam_dates: list[Exam] = field(default_factory=list)



# test = "37     lundi, septembre 11, 2023          TP2           mercredi, septembre 13, 2023        TP1            jeudi, septembre 14, 2023            TP3                    GRB            Semaine 37             TP3                           TP1                       FAUX"


# def extract_from_xslx(line: str, minimum_space_gap: int = 3) -> list[str]:
#     extraction = []
#     gap = minimum_space_gap * " "
#     line = line.split(gap)
#     for part in line:
#         if part != "":
#             part = part.strip()
#             extraction.append(part)
#     return extraction


# print(extract_from_xslx(test))


df = pd.read_csv("colloscope-Feuille-1.csv")
df["Horaire"] = df["Horaire"].str.replace(";", ",").str.strip("][").str.split(", ")
print(df.info())
print(df["Groupe"])
print(df.iloc[1]["Groupe"])
print(df[df["Semaine"] == 2])

# Par semaine : horaires et groupe associes

# Trinome.dispo : [date1, date2 ...]

GROUPS_TP = ["TP1", "TP2", "TP3"]
GROUPS_TAG = ["GRA", "GRB"]
ALL_GROUPS = GROUPS_TAG + GROUPS_TAG

def attributes_scheduled_trinoms(
    dataset: pd.DataFrame, all_groups: list[Trinomes]
) -> None:
    # parcourir dataset
    # Pour chaque row, if tp1, alros on ajoute a tp1.working_hours (semaine, jour, horaire)
    for row in dataset:
        if row["Groupe"] in GROUPS_TAG:
            for group in all_groups:
                if group.group_nb == row["Groupe"]:
                    group.working_hours.append(
                        (row["Semaine"], row["Date"], row["Horaire"])
                    )
        elif row["Groupe"] in GROUPS_TP:
            for group in all_groups:
                if group.group_nb == row["Groupe"]:
                    group.working_hours.append(
                        (row["Semaine"], row["Date"], row["Horaire"])
                    )
        else:
            for group in all_groups:
                group.working_hours.append(
                    (row["Semaine"], row["Date"], row["Horaire"])
                )
    return None

# def fetch_from_groups(all_groups: list[]) -> WorkingHour:
#     return 


def all_groups_list(amount_groups: int) -> list:
    group_list = []
    for index in range(1, amount_groups + 1):
        if index <= (amount_groups + 1) /3 and index <= (amount_groups + 1)/2:
            group_list.append(Trinomes(id=index, group_nb=1, group_tp="A"))
        elif index <= 2*(amount_groups + 1)/3 and index <= (amount_groups + 1)/2:
            group_list.append(Trinomes(id=index, group_nb=2, group_tp="A")) 
        elif index <= 2*(amount_groups + 1)/3:
            group_list.append(Trinomes(id=index, group_nb=2, group_tp="B"))
        else:
            group_list.append(Trinomes(id=index, group_nb=3, group_tp="B"))
    return group_list
# Input: Nb de groupes 

# Output: liste avec Nb de groupes trinomes appartenant à la classe trinomes  