from pandas import read_csv
from pathlib import Path
from ..data_classes import Trinome


class TrinomesFactory:
    def create(path_to_trinomes_csv: Path) -> list[Trinome]:
        trinomes = []
        trinomes_csv = read_csv(path_to_trinomes_csv)
        for row in trinomes_csv:
            trinomes.append(
                Trinome(
                    id=row["num_trinomes"],
                    group_td=row["groupe_td"],
                    group_tp=row["groupe_tp"],
                )
            )
        return trinomes