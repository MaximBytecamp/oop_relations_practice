class StudentAccount:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self._points = 0
        self._level = "beginner"

    def add_points(self, value):
        if value < 0:
            raise ValueError("Баллы должны быть положительными")
        self._points += value
        self.update_level()

    def update_level(self):
        if self._points >= 100:
            self._level = "advanced"
        elif self._points >= 50:
            self._level = "intermediate"
        else:
            self._level = "beginner"

    def get_info(self):
        return f"Имя: {self.name}, Группа: {self.group}, Баллы: {self._points}, Уровень: {self._level}"


if __name__ == "__main__":
    student = StudentAccount("Анна", "РПО-1")
    student.add_points(25)
    student.add_points(50)
    print(student.get_info())




