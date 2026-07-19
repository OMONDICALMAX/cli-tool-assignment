# Project Management CLI Tool

A Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks. This application demonstrates object-oriented programming principles, file persistence using JSON, modular code organization, automated testing with `pytest`, and dependency management using `Pipenv`.

---

## Features

* Create and manage users
* Create projects and assign them to users
* Create tasks and assign them to projects
* Mark tasks as completed
* View users, projects, and tasks
* Store data permanently using JSON
* Rich terminal tables and formatted output using the **Rich** library
* Unit tests using **pytest**
* Modular, object-oriented design

---

## Technologies Used

* Python 3.12+
* argparse
* JSON
* Pipenv
* Rich
* pytest
* Git & GitHub

---

## Project Structure

```text
cli-tool-assignement/
│
├── data/
│   └── database.json
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── tests/
│   ├── test_user.py
│   ├── test_project.py
│   ├── test_task.py
│   └── test_storage.py
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── storage.py
│
├── main.py
├── cli.py
├── requirements.txt
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
```

---

## Object-Oriented Design

The application is built using four primary classes.

### Person

The base class that stores common user information.

**Attributes**

* name
* email

### User

Inherits from `Person`.

**Responsibilities**

* Owns multiple projects
* Adds and removes projects
* Retrieves projects
* Serializes data to JSON

### Project

Represents a project assigned to a user.

**Attributes**

* title
* description
* due_date
* tasks

**Responsibilities**

* Add tasks
* Retrieve tasks
* Serialize data

### Task

Represents work to be completed within a project.

**Attributes**

* title
* status
* assigned_to

**Responsibilities**

* Mark tasks as completed
* Serialize data

---

## Relationships

```text
Person
   │
   ▼
User
   │
   ├── Project
   │      │
   │      ├── Task
   │      ├── Task
   │      └── Task
   │
   └── Project
          │
          └── Task
```

* One User can own many Projects.
* One Project can contain many Tasks.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/OMONDICALMAX/cli-tool-assignment.git
cd cli-tool-assignement
```

### Install Pipenv

```bash
pip install pipenv
```

### Install dependencies

```bash
pipenv install
```

### Activate the virtual environment

```bash
pipenv shell
```

---

## Running the Application

Run the application using:

```bash
python3 main.py
```

---

## CLI Commands

### Add a User

```bash
python3 main.py add-user \
--name "Alex" \
--email "alex@gmail.com"
```

---

### List Users

```bash
python3 main.py list-users
```

---

### Add a Project

```bash
python3 main.py add-project \
--user "Alex" \
--title "CLI Tool" \
--description "Python Project Management CLI" \
--due-date "2026-08-31"
```

---

### List Projects

```bash
python3 main.py list-projects \
--user "Alex"
```

---

### Add a Task

```bash
python3 main.py add-task \
--project "CLI Tool" \
--title "Implement add-task" \
--assigned-to "Alex"
```

---

### List Tasks

```bash
python3 main.py list-tasks \
--project "CLI Tool"
```

---

### Complete a Task

```bash
python3 main.py complete-task \
--project "CLI Tool" \
--title "Implement add-task"
```

---

## Data Persistence

All application data is stored in:

```text
data/database.json
```

The application automatically:

* Saves users
* Saves projects
* Saves tasks
* Loads data when the application starts

---

## Testing

Run all tests using:

```bash
pipenv run pytest
```

Expected output:

```text
=============================
9 passed
=============================
```

---

## External Packages

This project uses the following external packages:

* Rich

  * Beautiful terminal tables
  * Colored CLI output

* pytest

  * Automated unit testing

---

## Error Handling

The application handles:

* Missing users
* Missing projects
* Empty task lists
* Invalid JSON files
* Missing database file

---

## Future Improvements

Potential enhancements include:

* Delete users, projects, and tasks
* Edit project details
* Task priorities
* Task due dates
* User authentication
* Search functionality
* Export reports to CSV or PDF
* SQLite database support

---

## Learning Outcomes

This project demonstrates:

* Object-Oriented Programming (OOP)
* Inheritance
* Encapsulation
* Class relationships
* File handling
* JSON serialization
* Command-Line Interface development
* Python modules and packages
* Automated testing with pytest
* Dependency management with Pipenv
* Git and GitHub workflow

---

## Author

**Calmax Omondi**

