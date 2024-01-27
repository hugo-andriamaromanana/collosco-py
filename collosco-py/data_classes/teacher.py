from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Teacher:
    name: str
    subject: str
    heures: list[float] = field(default_factory=list)
    all_days: list[str] = field(default_factory=list)
