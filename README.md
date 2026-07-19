# Project Structure
project-management-cli/
│
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
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
├── utils/
│   ├── __init__.py
│   ├── storage.py
│   └── helpers.py
│
└── tests/
    ├── test_user.py
    ├── test_project.py
    ├── test_task.py
    └── test_storage.py