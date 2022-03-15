from .value_object.email import Email
from .value_object.password import Password
from .value_object.username import Username


class User:
    def __init__(self, idUser: int, username: Username, email: Email, password: Password):
        self.idUser: int = idUser
        self.username: Username = username
        self.email: Email = email
        self.password: Password = password

    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.idUser == o.idUser
        return False
