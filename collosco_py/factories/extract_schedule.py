from pathlib import Path
from pandas import DataFrame, read_csv


def extract_scheduled_tp(scheduled_tp_path: Path) -> DataFrame:
    """
    read csv schedule_tp
    transform content of column "Horaire" into a tuple
    """
    scheduled_tp = read_csv(scheduled_tp_path)
    scheduled_tp["Horaire"] = (
        scheduled_tp["Horaire"].str.replace(";", ",").str.strip("][").str.split(", ")
    )
    return scheduled_tp
