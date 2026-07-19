import argparse

from models.user import User
from models.project import Project
from models.task import Task
from rich.console import Console
from rich.table import Table

console = Console()

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
        console.print("[bold yellow]No users found.[/bold yellow]")
        return

    table = Table(title="Users")

    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Email", style="magenta")
    table.add_column("Projects", justify="center")

    for user in users:
        table.add_row(
            str(user.user_id),
            user.name,
            user.email,
            str(len(user.projects))
        )

    console.print(table)


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
        console.print(f"[bold red]User '{args.user}' not found.[/bold red]")
        return

    if not user.projects:
        console.print(f"[bold yellow]{user.name} has no projects.[/bold yellow]")
        return

    table = Table(title=f"Projects for {user.name}")

    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Title", style="green")
    table.add_column("Due Date", style="yellow")
    table.add_column("Tasks", justify="center")

    for project in user.projects:
        table.add_row(
            str(project.project_id),
            project.title,
            project.due_date,
            str(len(project.tasks))
        )

    console.print(table)


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
        console.print(f"[bold red]Project '{args.project}' not found.[/bold red]")
        return

    if not project.tasks:
        console.print(
            f"[bold yellow]Project '{project.title}' has no tasks.[/bold yellow]"
        )
        return

    table = Table(title=f"Tasks for {project.title}")

    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Title", style="green")
    table.add_column("Status", style="yellow")
    table.add_column("Assigned To", style="magenta")

    for task in project.tasks:
        table.add_row(
            str(task.task_id),
            task.title,
            task.status,
            task.assigned_to
        )

    console.print(table)


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