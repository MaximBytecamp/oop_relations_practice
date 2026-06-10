class Employee:
    def __init__(self, name, position, base_salary):
        self.name = name
        self.position = position
        self._base_salary = base_salary
        self._bonus_rate = 0.1

    def calculate_salary(self):
        return self._base_salary + self._base_salary * self._bonus_rate


class Developer(Employee):
    def __init__(self, name, base_salary, closed_tasks):
        super().__init__(name, "Developer", base_salary)
        self.closed_tasks = closed_tasks

    def calculate_salary(self):
        # TODO: использовать защищённые атрибуты родителя
        pass


class Designer(Employee):
    def __init__(self, name, base_salary, layouts_count):
        super().__init__(name, "Designer", base_salary)
        self.layouts_count = layouts_count

    def calculate_salary(self):
        pass
