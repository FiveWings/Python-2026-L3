import curses
import os
import zipfile

import numpy as np

from .domains import Course, Student
from .input import read_courses, read_marks, read_students
from .output import show_courses, show_students_by_gpa

DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))

def calculate_gpa(student: Student, courses: list[Course]) -> float:
    marks = np.array(
        [student.marks[course.course_id] for course in courses]
    )
    credits = np.array([course.credits for course in courses])
    return np.average(marks, weights=credits)

def save_to_dat() -> None:
    text_files = [
        "students.txt",
        "courses.txt",
        "marks.txt",
    ]

    dat_file = os.path.join(DATA_FOLDER, "student.dat")

    if os.path.exists(dat_file):
        os.remove(dat_file)

    with zipfile.ZipFile(
        dat_file,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        for filename in text_files:
            file_path = os.path.join(DATA_FOLDER, filename)

            if os.path.exists(file_path):
                archive.write(file_path, arcname=filename)

    print("Data saved and compressed to student.dat")

def load_from_dat() -> None:
    dat_file = os.path.join(DATA_FOLDER, "student.dat")

    with zipfile.ZipFile(dat_file, "r") as archive:
        archive.extractall(DATA_FOLDER)

    print("Existing data was decompressed.")

def load_students() -> list[Student]:
    students = []

    students_file = os.path.join(DATA_FOLDER, "students.txt")

    with open(students_file, "r") as file:
        for line in file:
            student_id, name, dob = [
                value.strip()
                for value in line.split(" | ")
            ]

            student = Student(
                name,
                student_id,
                dob,
            )

            students.append(student)
    return students

def load_courses() -> list[Course]:
    courses = []

    courses_file = os.path.join(DATA_FOLDER, "courses.txt")

    with open(courses_file, "r") as file:
        for line in file:
            course_id, name, credits = [
                value.strip()
                for value in line.split(" | ")
            ]

            course = Course(
                course_id,
                name,
                float(credits),
            )

            courses.append(course)
    return courses

def load_marks(students: list[Student]) -> None:
    students_by_id = {}

    for student in students:
        students_by_id[student.student_id] = student

    marks_file = os.path.join(DATA_FOLDER, "marks.txt")

    with open(marks_file, "r") as file:
        for line in file:
            student_id, course_id, mark = [
                value.strip()
                for value in line.split(" | ")
            ]

            student = students_by_id[student_id]
            student.marks[course_id] = float(mark)

def main(screen) -> None:
    curses.echo()
    screen.addstr("hello student gpa\n\n")
    screen.refresh()

    dat_file = os.path.join(DATA_FOLDER, "student.dat")

    if os.path.exists(dat_file):
        load_from_dat()

        students = load_students()
        courses = load_courses()
        load_marks(students)
    else:
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
    try:
        curses.wrapper(main)
    finally:
        save_to_dat()
