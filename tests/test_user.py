from models.user import User
from models.project import Project


def test_create_user():
    user = User("Alex", "alex@gmail.com")

    assert user.name == "Alex"
    assert user.email == "alex@gmail.com"
    assert user.projects == []


def test_add_project():
    user = User("Alex", "alex@gmail.com")
    project = Project(
        "CLI Tool",
        "Project Manager",
        "2026-08-31"
    )

    user.add_project(project)

    assert len(user.projects) == 1
    assert user.projects[0].title == "CLI Tool"


def test_get_project():
    user = User("Alex", "alex@gmail.com")

    project = Project(
        "CLI Tool",
        "Project Manager",
        "2026-08-31"
    )

    user.add_project(project)

    assert user.get_project("CLI Tool") == project