import math

from .domains import Course, Student


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
        date_of_birth = get_input(screen, f"Date of birth of {name}: ")
        students.append(Student(name, student_id, date_of_birth))

    return students


def read_courses(screen) -> list[Course]:
    count = int(get_input(screen, "How many courses? "))
    courses = []

    for number in range(count):
        course_id = get_input(screen, f"ID of course {number + 1}: ")
        course_name = get_input(screen, f"Name of course {course_id}: ")
        credits = float(get_input(screen, f"Credits for {course_name}: "))
        courses.append(Course(course_id, course_name, credits))

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
