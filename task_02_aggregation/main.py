class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    def add_grade(self, grade: int):
        self.grades.append(grade)

    def get_average(self) -> float:
        print(f"Средний балл студента: {self.first_name}: ")
        return sum(self.grades) / len(self.grades)


class Group:
    def __init__(self, title: str):
        self.title = title
        self.students = [] #Student(max, makarov, [4,5])

    def add_student(self, student: Student):
        self.students.append(student)

    def get_group_average(self) -> float:
        total_grades_list = []
        for student in self.students:
            total_grades_list.extend(student.grades) #[] -> [4,5] -> [4,5].extend([5,5]) -> [4,5,5,5]

        print(f"Средний балл группы: {sum(total_grades_list) / len(self.students)}")

    def print_students(self):
        for student in self.students: 
            print(f"{student.first_name} {student.last_name} - {student.get_average()}")



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


group.get_group_average()
