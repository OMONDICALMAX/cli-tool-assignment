from models.project import Project
from models.task import Task


def test_create_project():
    project = Project(
        "CLI Tool",
        "Python CLI",
        "2026-08-31"
    )

    assert project.title == "CLI Tool"
    assert project.tasks == []


def test_add_task():
    project = Project(
        "CLI Tool",
        "Python CLI",
        "2026-08-31"
    )

    task = Task(
        "Implement CLI",
        "Alex"
    )

    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Implement CLI"


def test_get_task():
    project = Project(
        "CLI Tool",
        "Python CLI",
        "2026-08-31"
    )

    task = Task(
        "Implement CLI",
        "Alex"
    )

    project.add_task(task)

    assert project.get_task("Implement CLI") == task