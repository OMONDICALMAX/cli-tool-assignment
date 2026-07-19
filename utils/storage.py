import json
from pathlib import Path

from models.user import User

DATABASE = Path(__file__).resolve().parent.parent / "data" / "database.json"


def save_data(users):
    """Save all users to the JSON database."""

    data = {
        "users": [user.to_dict() for user in users]
    }

    # Ensure the data directory exists
    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    with DATABASE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    """Load users from the JSON database."""

    if not DATABASE.exists():
        return []

    try:
        with DATABASE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            User.from_dict(user_data)
            for user_data in data.get("users", [])
        ]

    except json.JSONDecodeError:
        print("Error: Database file is corrupted.")
        return []

    except OSError as error:
        print(f"Error reading database: {error}")
        return []


def find_user(users, name):
    """Find a user by name."""

    for user in users:
        if user.name.lower() == name.lower():
            return user

    return None