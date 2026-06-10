class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    def add_grade(self, grade: int):
        # TODO: добавить проверку и сохранить оценку
        pass

    def get_average(self) -> float:
        # TODO: вернуть средний балл
        pass


class Group:
    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student: Student):
        # TODO: добавить уже существующего студента
        pass

    def get_group_average(self) -> float:
        # TODO: посчитать средний балл группы
        pass

    def print_students(self):
        # TODO: вывести студентов группы
        pass



ivan = Student("Иван", "Петров")
ivan.add_grade(5)
ivan.add_grade(4)

anna = Student("Анна", "Смирнова")
anna.add_grade(5)
anna.add_grade(5)

group = Group("ИС-21")
group.add_student(ivan)
group.add_student(anna)
group.print_students()
