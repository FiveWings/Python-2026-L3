#i love python (i am saying this voluntarily and without any external forces)

import builtins
import math


class Student:
    """Represents a student with name, ID, and date of birth."""

    def __init__(self, name="", student_id="", dob=""):
        self.__name = name          # private attributes
        self.__student_id = student_id
        self.__dob = dob

    # --- Getters (encapsulation) ---
    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def dob(self):
        return self.__dob

    # --- Polymorphic interface ---
    def input(self, index=None):
        """Prompt user to enter student info."""
        label = f" number {index}" if index is not None else ""
        self.__name = builtins.input(f"Enter name for student{label}: ")
        self.__student_id = builtins.input("Enter ID for student: ")
        self.__dob = builtins.input("Enter day of birth of student: ")

    def list(self):
        """Display this student's details."""
        print(f"ID: {self.__student_id} | Name: {self.__name} | DoB: {self.__dob}")

    def __str__(self):
        return f"{self.__name} ({self.__student_id})"


class Course:
    """Represents a course with an ID and name."""

    def __init__(self, course_id="", name=""):
        self.__course_id = course_id  # private attributes
        self.__name = name

    # --- Getters (encapsulation) ---
    @property
    def course_id(self):
        return self.__course_id

    @property
    def name(self):
        return self.__name

    # --- Polymorphic interface ---
    def input(self, index=None):
        """Prompt user to enter course info."""
        label = f" number {index}" if index is not None else ""
        self.__course_id = builtins.input(f"For course{label}, enter ID: ")
        self.__name = builtins.input("Enter course name: ")

    def list(self):
        """Display this course's details."""
        print(f"ID: {self.__course_id} | Name: {self.__name}")

    def __str__(self):
        return f"{self.__name} ({self.__course_id})"


class MarkSheet:
    """Stores and manages marks for a single course."""

    def __init__(self, course):
        self.__course = course       # private: associated Course object
        self.__marks = {}            # private: {student_id: score}

    @property
    def course(self):
        return self.__course

    def input(self, students):
        """Prompt user to enter marks for every student in the given list."""
        print(f"\nEntering marks for course: {self.__course.course_id}")
        for s in students:
            score = float(builtins.input(f"Mark for {s.name} and ({s.student_id}): "))
            self.__marks[s.student_id] = score

    def get_mark(self, student_id):
        """Return a student's mark, or 'N/A' if not recorded."""
        return self.__marks.get(student_id, "N/A")

    def list(self, students):
        """Display marks for this course."""
        print(f"\n=== Marks for Course {self.__course.course_id} ===")
        for s in students:
            score = self.get_mark(s.student_id)
            print(f"{s.name} ({s.student_id}): {score}")


class SchoolManager:
    """Top-level manager that ties Students, Courses, and Marks together."""

    def __init__(self):
        self.__students = []         # private lists
        self.__courses = []
        self.__mark_sheets = {}      # {course_id: MarkSheet}

    # ---------- input helpers ----------
    def input_students(self):
        """Ask user for the number of students, then input each one."""
        num = int(builtins.input("Enter the number of students: "))  #ts is self-explanatory
        for i in range(num):
            s = Student()
            s.input(i + 1)           # polymorphic .input()
            self.__students.append(s)

    def input_courses(self):
        """Ask user for the number of courses, then input each one."""
        num = int(builtins.input("\nEnter number of courses: "))
        for i in range(num):
            c = Course()
            c.input(i + 1)          # polymorphic .input()
            self.__courses.append(c)

    def input_marks(self):
        """Let user select a course and enter marks for all students."""
        if not self.__courses:
            print("No courses found.")
            return
        if not self.__students:
            print("No students found.")
            return

        print("List of courses: ")
        for c in self.__courses:
            c.list()                # polymorphic .list()

        selected_id = builtins.input("Select a course ID: ")

        #if i cannot find the course, kys
        course_obj = self.__find_course(selected_id)
        if course_obj:              # enter each losers' point for each course
            ms = MarkSheet(course_obj)
            ms.input(self.__students)
            self.__mark_sheets[selected_id] = ms
        else:
            print("Course not found!")  #kys

    # ---------- list helpers ----------
    def list_courses(self):
        """Print all courses."""
        print("\n=== Course List ===")
        for c in self.__courses:
            c.list()                # polymorphic .list()

    def list_students(self):
        """Print all students."""
        print("\n=== Student List ===")
        for s in self.__students:
            s.list()                # polymorphic .list()

    def list_marks(self):
        """Ask for a course ID and display the marks."""
        view_cid = builtins.input("\nEnter Course ID to view marks: ")
        if view_cid in self.__mark_sheets:
            self.__mark_sheets[view_cid].list(self.__students)
        else:
            print("No marks recorded for this course.")

    # ---------- private helpers ----------
    def __find_course(self, course_id):
        """Return the Course with the given ID, or None."""
        for c in self.__courses:
            if c.course_id == course_id:
                return c
        return None


# ======================== main ========================
if __name__ == "__main__":
    manager = SchoolManager()

    manager.input_students()
    manager.input_courses()
    manager.input_marks()

    manager.list_courses()
    manager.list_students()
    manager.list_marks()
