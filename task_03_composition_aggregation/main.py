class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Lesson:
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration


class Module:
    def __init__(self, title: str):
        self.title = title
        self.lessons = []

    def add_lesson(self, title: str, duration: int):
        lesson = Lesson(title, duration)
        self.lessons.append(lesson)


class OnlineCourse:
    def __init__(self, title: str, teacher: User = None):
        self.title = title
        self.teacher = teacher
        self.students = []
        self.modules = []

    def enroll_student(self, student: User):
        self.students.append(student)


    def add_module(self, title: str) -> Module:
        module = Module(title)
        self.modules.append(module)
        return module

    def print_course_info(self):
        print(f"Курс: {self.title}")
        print(f"Преподаватель: {self.teacher.name} ({self.teacher.email})")

        print("Студенты:")
        for student in self.students:
            print(f"- {student.name} ({student.email})")

        print("Модули:")
        for module in self.modules:
            print(f"- {module.title}")
            for lesson in module.lessons:
                print(f"  - {lesson.title} ({lesson.duration} мин)")


# Агрегация:
teacher = User("Мария", "maria@example.com")
student = User("Олег", "oleg@example.com")
course = OnlineCourse("Основы Python", teacher)
course.enroll_student(student)

# Композиция:
module = course.add_module("ООП")
module.add_lesson("Классы и объекты", 45)
module.add_lesson("Композиция и агрегация", 60)

course.print_course_info()