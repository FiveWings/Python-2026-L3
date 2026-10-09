import math
import os

from .domains import Course, Student

DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))


def get_input(screen, message: str) -> str:
    screen.clear()
    screen.addstr(message)
    screen.refresh()
    return screen.getstr().decode("utf-8").strip()


def read_students(screen) -> list[Student]:
    count = int(get_input(screen, "How many students? "))
    students = []

    for number in range(count):
        name = get_input(screen, f"Name of student {number + 1}: ")
        student_id = get_input(screen, f"ID of {name}: ")
        dob = get_input(screen, f"Date of birth of {name}: ")
        students.append(Student(name, student_id, dob))

    with open(
        os.path.join(DATA_FOLDER, "students.txt"),
        "w",
        encoding="utf-8",
    ) as file:
        for student in students:
            file.write(
                f"{student.student_id} | {student.name} | {student.dob}\n"
            )

    return students


def read_courses(screen) -> list[Course]:
    count = int(get_input(screen, "How many courses? "))
    courses = []

    for number in range(count):
        course_id = get_input(screen, f"ID of course {number + 1}: ")
        course_name = get_input(screen, f"Name of course {course_id}: ")
        credits = float(get_input(screen, f"Credits for {course_name}: "))
        courses.append(Course(course_id, course_name, credits))

    with open(
        os.path.join(DATA_FOLDER, "courses.txt"),
        "w",
        encoding="utf-8",
    ) as file:
        for course in courses:
            file.write(
                f"{course.course_id} | {course.name} | {course.credits}\n"
            )

    return courses


def read_marks(screen, students: list[Student], courses: list[Course]) -> None:
    for course in courses:
        for student in students:
            message = (
                f"GPA mark for {student.name} ({student.student_id})\n"
                f"Course: {course.name} ({course.course_id})\n"
                f"Enter mark: "
            )
            score = float(get_input(screen, message))
            student.marks[course.course_id] = math.floor(score * 10) / 10

    with open(
        os.path.join(DATA_FOLDER, "marks.txt"),
        "w",
        encoding="utf-8",
    ) as file:
        for student in students:
            for course_id, mark in student.marks.items():
                file.write(
                    f"{student.student_id} | {course_id} | {mark}\n"
                )
