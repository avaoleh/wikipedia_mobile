from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
    fake_username: str
    fake_password: str


user = User(
    username='test_user_oao',
    password='qwerty123',
    fake_username='Tom_Mobile_Cruise',
    fake_password='8hBXgbkiJxWl'
)
