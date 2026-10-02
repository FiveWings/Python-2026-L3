from dataclasses import dataclass


@dataclass
class Course:
    course_id: str
    name: str
    credits: float
