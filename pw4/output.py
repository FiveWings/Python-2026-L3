def pause(screen) -> None:
    screen.addstr("\nPress any key to continue...")
    screen.refresh()
    screen.getch()


def show_courses(screen, courses) -> None:
    screen.clear()
    screen.addstr("COURSES\n\n")

    for course in courses:
        screen.addstr(
            f"{course.course_id} | {course.name} | "
            f"{course.credits:.1f} credits\n"
        )

    pause(screen)


def show_students_by_gpa(screen, students) -> None:
    screen.clear()
    screen.addstr("STUDENTS SORTED BY GPA\n\n")

    for number, student in enumerate(students, start=1):
        screen.addstr(
            f"{number}. {student.name} ({student.student_id}) - "
            f"GPA: {student.gpa:.2f}\n"
        )

    pause(screen)
