import pandas as pd
from collections import Counter
from ast import literal_eval
import datetime
import re

from .data_classes import Trinome

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

# Par semaine : horaires et groupe associes

# Trinome.dispo : [date1, date2 ...]


# def fetch_from_groups(all_groups: list[]) -> WorkingHour:
#     return


# def all_groups_list(amount_groups: int) -> list[Trinome]:
#     group_str = "1"*4+"2"*4+
#     group_list = []
#     for index in range(1, amount_groups + 1):
#         if (
#             index <= (amount_groups + 1) / 3 and index <= (amount_groups + 1) / 2
#         ):  # C'est l'inverse pour les conditions non ?
#             group_list.append(Trinome(id=index, group_nb=1, group_tp="A"))
#         elif index <= 2 * (amount_groups + 1) / 3 and index <= (amount_groups + 1) / 2:
#             group_list.append(Trinome(id=index, group_nb=2, group_tp="A"))
#         elif index <= 2 * (amount_groups + 1) / 3:
#             group_list.append(Trinome(id=index, group_nb=2, group_tp="B"))
#         else:
#             group_list.append(Trinome(id=index, group_nb=3, group_tp="B"))
#     return group_list

# case 1 : 0 < id <= amount_groups/3 => grp 1 tp A
# case 2 : amount_groups/3 < id <= amount_groups/2 => grp 2 tp A
# case 3 : amount_groups/2 < id <= 2*amount_groups3/3 => grp 2 tp B
# case 4 : grp 3 tp B


# context  : the daframe column "Groupe" has basicly 3 main values : TPx, GRx, othe
# cond1:
# Because they are not separated, we need to figure if the group of the Trinome = of row["Groupe"] but also if the tp of the Trinome = row["Groupe"]
# If it is other, it will be added for everyone

# Input: Nb de groupes

# Output: liste avec Nb de groupes Trinome appartenant à la classe Trinome

# Title : read csv of schedules tp & td
# step 1 : extract the csv
# step 2 : transform csv (horaire -> list) -> scheduled_tp
# -- missing : create groups (Trinome)
# step 3 : want to put hours of the dataset into corresponding groups
# -> function with :
# input : a dataframe (scheduled_tp) and the list of created groups (Trinome)
# Output : a modified group, each group has in a list of UnavailableTime of tp.
# Content : iterate through the list of Trinome and iterate for each row of the dataframe (scheduled_tp), if the row["Groupe"] is the same as the Trinome tp group or group, we will had in the trinome
# The unavailiable time of the row


# T1,Grp TP-1,Grp TD-A
# T2,Grp TP-1,Grp TD-A