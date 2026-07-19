from models.user import User
from utils.storage import save_data, load_data


def test_save_and_load():
    user = User(
        "Alex",
        "alex@gmail.com"
    )

    save_data([user])

    users = load_data()

    assert len(users) >= 1
    assert users[0].name == "Alex"