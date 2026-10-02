import curses
import math
import numpy as np


def get_input(screen, message): #show stuffs and wait for input
    screen.clear()
    screen.addstr(message)
    screen.refresh()
    return screen.getstr().decode("utf-8")


def pause(screen): #wait
    screen.addstr("\nPress any key to continue...")
    screen.refresh()
    screen.getch()


def calc_gpa(student_id, courses, marks): #def to calculate gpa
    student_marks = []
    course_credits = []

    for course in courses:
        course_id = course["id"]

        if student_id in marks[course_id]:
            student_marks.append(marks[course_id][student_id])
            course_credits.append(course["credits"])

    mark_array = np.array(student_marks)
    credit_array = np.array(course_credits)

    return np.average(mark_array, weights=credit_array)


def main(screen):
    curses.echo()

    screen.addstr("NICE LABWORK\n\n")
    number_of_students = int(
        get_input(screen, "Number of students: ")
    )

    students = []
    for number in range(number_of_students):
        student_number = number + 1
        name = get_input(
            screen,
            f"Enter the name for student {student_number}: ",
        )
        student_id = get_input(
            screen,
            f"Enter the ID for student {student_number} ({name}): ",
        )
        date_of_birth = get_input(
            screen,
            f"Enter the date of birth for student {student_number} "
            f"({name}): ",
        )

        students.append({
            "name": name,
            "id": student_id,
            "dob": date_of_birth,
        })

    screen.addstr("\n")
    number_of_courses = int(
        get_input(screen, "Number of courses: ")
    )

    courses = []
    for number in range(number_of_courses):
        course_number = number + 1
        course_id = get_input(
            screen,
            f"Enter the ID for course {course_number}: ",
        )
        course_name = get_input(
            screen,
            f"Enter the name for course {course_number} "
            f"({course_id}): ",
        )
        credits = float(
            get_input(
                screen,
                f"Enter the number of credits for course "
                f"{course_name} ({course_id}): ",
            )
        )

        courses.append({
            "id": course_id,
            "name": course_name,
            "credits": credits,
        })

    marks = {}
    for course in courses:
        course_id = course["id"]
        marks[course_id] = {}

        for student in students:
            score = float(
                get_input(
                    screen,
                    f"Enter the GPA mark for student "
                    f"{student['name']} ({student['id']}) "
                    f"in course {course['name']} ({course_id}): ",
                )
            )
            score = math.floor(score * 10) / 10
            marks[course_id][student["id"]] = score

    for student in students:
        student["gpa"] = calc_gpa(
            student["id"],
            courses,
            marks,
        )

    students.sort(
        key=lambda student: student["gpa"],
        reverse=True,
    )

    screen.clear()
    screen.addstr("STUDENTS SORTED BY GPA\n\n")
    for number, student in enumerate(students, start=1):
        screen.addstr(
            f"{number}. {student['name']} "
            f"({student['id']}) - "
            f"GPA: {student['gpa']:.2f}\n"
        )

    pause(screen)


if __name__ == "__main__":
    curses.wrapper(main)
