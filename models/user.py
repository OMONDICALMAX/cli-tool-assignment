from models.person import Person


class User(Person):
    """Represents a user who can own multiple projects."""

    next_id = 1

    def __init__(self, name: str, email: str):
        super().__init__(name, email)

        self.user_id = User.next_id
        User.next_id += 1

        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def remove_project(self, title):
        self.projects = [
            project for project in self.projects
            if project.title != title
        ]

    def get_project(self, title):
        for project in self.projects:
            if project.title == title:
                return project
        return None

    def __str__(self):
        return (
            f"User #{self.user_id}: "
            f"{self.name} | "
            f"{len(self.projects)} project(s)"
        )