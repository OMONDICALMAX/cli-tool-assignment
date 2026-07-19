class Task:
    """Represents a project task."""

    next_id = 1

    def __init__(self, title: str, assigned_to: str):
        self.task_id = Task.next_id
        Task.next_id += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ("Pending", "Completed")

        if value not in allowed:
            raise ValueError("Status must be 'Pending' or 'Completed'.")

        self._status = value

    def complete(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["title"],
            data["assigned_to"]
        )

        task.task_id = data["task_id"]
        task.status = data["status"]

        if task.task_id >= cls.next_id:
            cls.next_id = task.task_id + 1

        return task

    def __str__(self):
        return (
            f"Task #{self.task_id}: "
            f"{self.title} "
            f"[{self.status}] "
            f"Assigned to: {self.assigned_to}"
        )