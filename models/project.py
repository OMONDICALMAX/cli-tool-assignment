from models.task import Task


class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        return task

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def __str__(self):
        return self.title