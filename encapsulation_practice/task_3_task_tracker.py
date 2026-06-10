class Task:
    ALLOWED_STATUSES = ["new", "in_progress", "review", "done"]

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.__status = "new"
        self._history = ["Создана задача со статусом new"]

    @property
    def status(self):
        pass

    @status.setter
    def status(self, value):
        pass

    def get_history(self):
        pass


if __name__ == "__main__":
    task = Task("Сделать README", "Описать запуск проекта")
    task.status = "in_progress"
    task.status = "review"
    print(task.status)
    print(task.get_history())
