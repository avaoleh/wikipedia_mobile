from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
    fake_username: str
    fake_password: str


user = User(
    username='test_user',
    password='qwerty123',
    fake_username='Tom_Cruise',
    fake_password='8hBXgbkiJxWl'
)
