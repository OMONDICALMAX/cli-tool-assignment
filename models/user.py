from models.project import Project


class User:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, title):
        project = Project(title)
        self.projects.append(project)
        return project

    def get_project(self, title):
        for project in self.projects:
            if project.title == title:
                return project
        return None

    def __str__(self):
        return self.name