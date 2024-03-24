from pandas import read_csv
from pathlib import Path

from ..data_objects.group_objects import Trinome

def create_trinomes(path_to_trinomes_csv: Path) -> list[Trinome]:
    trinomes = []
    trinomes_csv = read_csv(path_to_trinomes_csv)
    for _, row in trinomes_csv.iterrows():
        trinomes.append(
            Trinome(
                id=row["num_trinomes"],
                group_td=row["groupe_td"],
                group_tp=row["groupe_tp"],
            )
        )
    return trinomes
