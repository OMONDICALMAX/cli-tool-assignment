from models.person import Person
from models.project import Project


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

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "projects": [
                project.to_dict()
                for project in self.projects
            ]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data["name"],
            data["email"]
        )

        user.user_id = data["user_id"]

        if user.user_id >= cls.next_id:
            cls.next_id = user.user_id + 1

        user.projects = [
            Project.from_dict(project_data)
            for project_data in data["projects"]
        ]

        return user

    def __str__(self):
        return (
            f"User #{self.user_id}: "
            f"{self.name} | "
            f"{len(self.projects)} project(s)"
        )