from datetime import timedelta
from pathlib import Path
from pandas import DataFrame, read_csv, Series
from typing import Any, Tuple
from icecream import ic

def parse_horaire(raw_horaire: Series[Any]) -> Tuple[timedelta,timedelta]:
    return (timedelta(hours = raw_horaire[0][0]),timedelta(hours = raw_horaire[0][1]))

def extract_scheduled_tp(scheduled_tp_path: Path) -> DataFrame:
    """
    read csv schedule_tp
    transform content of column "Horaire" into a tuple
    """
    scheduled_tp = read_csv(scheduled_tp_path)
    raw_horaire = scheduled_tp["Horaire"].str.replace(";", ",").str.strip("][").str.split(", ")
    scheduled_tp["Horaire"] = parse_horaire(raw_horaire)
    return scheduled_tp


