import argparse

from models.user import User
from models.project import Project
from models.task import Task

from utils.storage import (
    load_data,
    save_data,
    find_user,
    find_project
)


# ======================================================
# USER COMMANDS
# ======================================================

def add_user(args):
    """Add a new user."""

    users = load_data()

    if find_user(users, args.name):
        print(f"User '{args.name}' already exists.")
        return

    try:
        user = User(args.name, args.email)
        users.append(user)

        save_data(users)

        print(f"User '{user.name}' added successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def list_users(args):
    """Display all users."""

    users = load_data()

    if not users:
        print("No users found.")
        return

    print("\nUsers")
    print("-" * 40)

    for user in users:
        print(user)


# ======================================================
# PROJECT COMMANDS
# ======================================================

def add_project(args):
    """Add a project to an existing user."""

    users = load_data()

    user = find_user(users, args.user)

    if user is None:
        print(f"User '{args.user}' not found.")
        return

    if user.get_project(args.title):
        print(f"Project '{args.title}' already exists.")
        return

    try:
        project = Project(
            args.title,
            args.description,
            args.due_date
        )

        user.add_project(project)

        save_data(users)

        print(
            f"Project '{project.title}' added "
            f"to user '{user.name}'."
        )

    except ValueError as error:
        print(f"Error: {error}")


def list_projects(args):
    """Display all projects belonging to a user."""

    users = load_data()

    user = find_user(users, args.user)

    if user is None:
        print(f"User '{args.user}' not found.")
        return

    if not user.projects:
        print(f"{user.name} has no projects.")
        return

    print(f"\nProjects for {user.name}")
    print("-" * 40)

    for project in user.projects:
        print(project)


# ======================================================
# CLI CONFIGURATION
# ======================================================

parser = argparse.ArgumentParser(
    description="Project Management CLI Tool"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

# ------------------------------------------------------
# add-user
# ------------------------------------------------------

add_user_parser = subparsers.add_parser(
    "add-user",
    help="Add a new user"
)

add_user_parser.add_argument(
    "--name",
    required=True,
    help="User's full name"
)

add_user_parser.add_argument(
    "--email",
    required=True,
    help="User's email address"
)

add_user_parser.set_defaults(
    func=add_user
)

# ------------------------------------------------------
# list-users
# ------------------------------------------------------

list_users_parser = subparsers.add_parser(
    "list-users",
    help="Display all users"
)

list_users_parser.set_defaults(
    func=list_users
)

# ------------------------------------------------------
# add-project
# ------------------------------------------------------

add_project_parser = subparsers.add_parser(
    "add-project",
    help="Add a project to a user"
)

add_project_parser.add_argument(
    "--user",
    required=True,
    help="User name"
)

add_project_parser.add_argument(
    "--title",
    required=True,
    help="Project title"
)

add_project_parser.add_argument(
    "--description",
    required=True,
    help="Project description"
)

add_project_parser.add_argument(
    "--due-date",
    dest="due_date",
    required=True,
    help="Project due date"
)

add_project_parser.set_defaults(
    func=add_project
)

# ------------------------------------------------------
# list-projects
# ------------------------------------------------------

list_projects_parser = subparsers.add_parser(
    "list-projects",
    help="Display projects for a user"
)

list_projects_parser.add_argument(
    "--user",
    required=True,
    help="User name"
)

list_projects_parser.set_defaults(
    func=list_projects
)
# ======================================================
# TASK COMMANDS
# ======================================================

def add_task(args):
    """Add a task to an existing project."""

    users = load_data()

    project = find_project(users, args.project)

    if project is None:
        print(f"Project '{args.project}' not found.")
        return

    if project.get_task(args.title):
        print(f"Task '{args.title}' already exists.")
        return

    try:
        task = Task(
            args.title,
            args.assigned_to
        )

        project.add_task(task)

        save_data(users)

        print(
            f"Task '{task.title}' added "
            f"to project '{project.title}'."
        )

    except ValueError as error:
        print(f"Error: {error}")


def list_tasks(args):
    """Display all tasks in a project."""

    users = load_data()

    project = find_project(users, args.project)

    if project is None:
        print(f"Project '{args.project}' not found.")
        return

    if not project.tasks:
        print(f"Project '{project.title}' has no tasks.")
        return

    print(f"\nTasks for {project.title}")
    print("-" * 50)

    for task in project.tasks:
        print(task)


def complete_task(args):
    """Mark a task as completed."""

    users = load_data()

    project = find_project(users, args.project)

    if project is None:
        print(f"Project '{args.project}' not found.")
        return

    task = project.get_task(args.title)

    if task is None:
        print(f"Task '{args.title}' not found.")
        return

    task.complete()

    save_data(users)

    print(f"Task '{task.title}' marked as completed.")


# ------------------------------------------------------
# add-task
# ------------------------------------------------------

add_task_parser = subparsers.add_parser(
    "add-task",
    help="Add a task to a project"
)

add_task_parser.add_argument(
    "--project",
    required=True,
    help="Project title"
)

add_task_parser.add_argument(
    "--title",
    required=True,
    help="Task title"
)

add_task_parser.add_argument(
    "--assigned-to",
    dest="assigned_to",
    required=True,
    help="Person assigned to the task"
)

add_task_parser.set_defaults(
    func=add_task
)

# ------------------------------------------------------
# list-tasks
# ------------------------------------------------------

list_tasks_parser = subparsers.add_parser(
    "list-tasks",
    help="Display all tasks in a project"
)

list_tasks_parser.add_argument(
    "--project",
    required=True,
    help="Project title"
)

list_tasks_parser.set_defaults(
    func=list_tasks
)

# ------------------------------------------------------
# complete-task
# ------------------------------------------------------

complete_task_parser = subparsers.add_parser(
    "complete-task",
    help="Mark a task as completed"
)

complete_task_parser.add_argument(
    "--project",
    required=True,
    help="Project title"
)

complete_task_parser.add_argument(
    "--title",
    required=True,
    help="Task title"
)

complete_task_parser.set_defaults(
    func=complete_task)


# ======================================================
# MAIN
# ======================================================

def main():
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()