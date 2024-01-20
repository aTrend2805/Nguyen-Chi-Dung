class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter student Date of Birth: ")

    def list(self):
        print(f"ID: {self.__id}, Name: {self.__name}, Date of Birth: {self.__dob}")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name

    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")

    def list(self):
        print(f"Course ID: {self.__id}, Name: {self.__name}")

    def get_id(self):
        return self.__id


class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        for _ in range(int(input("Enter the number of students: "))):
            student = Student(None, None, None)
            student.input()
            self.students.append(student)

    def input_courses(self):
        for _ in range(int(input("Enter the number of courses: "))):
            course = Course(None, None)
            course.input()
            self.courses.append(course)

    def select_course_and_input_marks(self):
        self.list_courses()
        course_id = input("Select a course ID to input marks: ")
        course = next((c for c in self.courses if c.get_id() == course_id), None)
        if course:
            for student in self.students:
                mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_id()}): "))
                self.marks.setdefault(course.get_id(), []).append((student.get_id(), mark))
        else:
            print("Course not found.")

    def list_courses(self):
        for course in self.courses:
            course.list()

    def list_students(self):
        for student in self.students:
            student.list()

    def show_student_marks_for_course(self, course_id):
        if course_id in self.marks:
            print(f"Marks for course {course_id}:")
            for student_id, mark in self.marks[course_id]:
                student = next(s for s in self.students if s.get_id() == student_id)
                print(f"Student {student.get_name()} (ID: {student.get_id()}): Mark: {mark}")
        else:
            print("No marks available for this course.")


def main():
    system = ManagementSystem()
    system.input_students()
    system.input_courses()
    system.select_course_and_input_marks()
    while True:
        print("\nOptions: 1. List Courses 2. List Students 3. Show Marks for a Course 4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            system.list_courses()
        elif choice == '2':
            system.list_students()
        elif choice == '3':
            course_id = input("Enter course ID to show marks: ")
            system.show_student_marks_for_course(course_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
