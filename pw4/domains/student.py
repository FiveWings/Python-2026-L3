from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    student_id: str
    date_of_birth: str
    marks: dict[str, float] = field(default_factory=dict)
    gpa: float = 0.0
