from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    student_id: str
    dob: str
    marks: dict[str, float] = field(default_factory=dict)
    gpa: float = 0.0
