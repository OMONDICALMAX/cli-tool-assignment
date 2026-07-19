from models.task import Task


def test_create_task():
    task = Task(
        "Implement CLI",
        "Alex"
    )

    assert task.title == "Implement CLI"
    assert task.assigned_to == "Alex"
    assert task.status == "Pending"


def test_complete_task():
    task = Task(
        "Implement CLI",
        "Alex"
    )

    task.complete()

    assert task.status == "Completed"