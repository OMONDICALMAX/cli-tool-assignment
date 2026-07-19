class Project:
    """Represents a project."""

    next_id = 1

    def __init__(self, title: str, description: str, due_date: str):
        self.project_id = Project.next_id
        Project.next_id += 1

        self.title = title
        self.description = description
        self.due_date = due_date

        self.tasks = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        value = value.strip()

        if not value:
            raise ValueError("Project title cannot be empty.")

        self._title = value

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def __str__(self):
        return (
            f"Project #{self.project_id}: "
            f"{self.title} "
            f"({len(self.tasks)} task(s))"
        )