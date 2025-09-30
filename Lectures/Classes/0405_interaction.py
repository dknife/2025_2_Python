class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
            print(f"{self.name} enrolled in {course.title}")

    def list_courses(self):
        print(f"{self.name} is enrolled in:")
        for course in self.courses:
            print(f"- {course.title}")

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def list_students(self):
        print(f"Students enrolled in {self.title}:")
        for student in self.students:
            print(f"- {student.name}")

# Example usage
math = Course("Mathematics")
science = Course("Science")

alice = Student("Alice")
bob = Student("Bob")

alice.enroll(math)
alice.enroll(science)
bob.enroll(math)

math.list_students()
alice.list_courses()