
students = []
courses = []
marks = {}


def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    for _ in range(input_number_of_students()):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Date of Birth: ")
        students.append({"id": student_id, "name": student_name, "DoB": student_dob})

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    for _ in range(input_number_of_courses()):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({"id": course_id, "name": course_name})

def select_course_and_input_marks():
    list_courses()
    course_id = input("Select a course ID to input marks: ")
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        marks.setdefault(course_id, []).append((student['id'], mark))


def list_courses():
    for course in courses:
        print(f"Course ID: {course['id']}, Name: {course['name']}")

def list_students():
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Date of Birth: {student['DoB']}")

def show_student_marks_for_course(course_id):
    if course_id in marks:
        print(f"Marks for course {course_id}:")
        for student_id, mark in marks[course_id]:
            student = next(s for s in students if s["id"] == student_id)
            print(f"Student {student['name']} (ID: {student['id']}): Mark: {mark}")
    else:
        print("No marks available for this course.")


def main():
    input_student_info()
    input_course_info()
    select_course_and_input_marks()
    while True:
        print("\nOptions: 1. List Courses 2. List Students 3. Show Marks for a Course 4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_courses()
        elif choice == '2':
            list_students()
        elif choice == '3':
            course_id = input("Enter course ID to show marks: ")
            show_student_marks_for_course(course_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
