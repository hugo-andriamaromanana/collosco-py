from dataclasses import dataclass


@dataclass(kw_only=True)
class Student:
    group_name: str
    group_nb: int
    group_tp: str
    tag: str
