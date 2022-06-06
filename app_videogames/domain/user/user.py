from app_videogames.domain.user.value_object import (Email, Password, Username)


class User:

    def __init__(self, id_user: int, username: Username, email: Email, password: Password):
        self.id_user: int = id_user
        self.username: Username = username
        self.email: Email = email
        self.password: Password = password

    def get_safe_user(self):
        return {
           'idUser': self.idUser,
           'username': self.username,
           'email': self.email
       }

    @staticmethod
    def get_safe_users(list_users: list):
        for user in list_users:
            del user.password
        return list_users
