#i love python (i am saying this voluntarily and without any external forces)

num_students = int(input("Enter the number of students:")) #ts is self-explanatory
students = []

for i in range(num_students): #ask info of each of the losers in the class
    name = input(f"Enter name for student number {i + 1}: ")
    student_id = input("Enter ID for student: ")
    dob = input("Enter day of birth of student: ")
    students.append({"name": name, "id": student_id, "dob": dob})
num_courses = int(input("\nEnter number of courses: "))
courses = []

for i in range(num_courses): #ask info of each level of hell
    course_id = input(f"For course number {i + 1}, enter ID: ")
    course_name = input("Enter course name: ")
    courses.append({"id": course_id, "name": course_name})

if not courses:
    print("No courses found.")
if not students:
    print("No students found")
else:
    print("List of courses: ")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

mark = {}
selected_course = input("Select a course ID: ")

#if i cannot find the course, kys
course_found = False
for course in courses:
    if course["id"] == selected_course:
        course_found = True
        break

if course_found: #enter each losers' point for each course
    mark[selected_course] = {}
    print(f"\nEntering marks for course: {selected_course}")
    for s in students:
        marks = float(input(f"Mark for {s['name']} and ({s['id']})"))
        mark[selected_course][s['id']] = marks
else:
    print("Course not found!") #kys
print("\n=== Course List ===")
for c in courses:
    print(f"ID: {c['id']} | Name: {c['name']}")


print("\n=== Student List ===")
for s in students:
    print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")


view_cid = input("\nEnter Course ID to view marks: ")

if view_cid in mark:
    print(f"\n=== Marks for Course {view_cid} ===")
    for s in students:
        sid = s["id"]
        score = mark[view_cid].get(sid, "N/A")
        print(f"{s['name']} ({sid}): {score}")
else:
    print("No marks recorded for this course.")

