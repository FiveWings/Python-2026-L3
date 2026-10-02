import curses

import numpy as np

from .domains import Course, Student
from .input import read_courses, read_marks, read_students
from .output import show_courses, show_students_by_gpa


def calculate_gpa(student: Student, courses: list[Course]) -> float:
    marks = np.array(
        [student.marks[course.course_id] for course in courses]
    )
    credits = np.array([course.credits for course in courses])
    return np.average(marks, weights=credits)


def main(screen) -> None:
    curses.echo()
    screen.addstr("STUDENT GPA PROGRAM\n\n")
    screen.refresh()

    students = read_students(screen)
    courses = read_courses(screen)
    read_marks(screen, students, courses)
    show_courses(screen, courses)

    for student in students:
        student.gpa = calculate_gpa(student, courses)

    students.sort(
        key=lambda student: student.gpa,
        reverse=True,
    )
    show_students_by_gpa(screen, students)


if __name__ == "__main__":
    curses.wrapper(main)
