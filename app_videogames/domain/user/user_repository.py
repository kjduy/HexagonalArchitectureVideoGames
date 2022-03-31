from abc import abstractmethod

from .user import User
from app_videogames.infrastructure.sqlite.user.user_create_model import UserCreateModel
from app_videogames.infrastructure.sqlite.user.user_update_model import UserUpdateModel


class UserRepository:

    @abstractmethod
    def get_users(self) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, id_user: int) -> User:
        pass

    @abstractmethod
    def insert_user(self, user: UserCreateModel) -> str:
        pass

    @abstractmethod
    def update_user(self, id_user: int, user: UserUpdateModel) -> str:
        pass

    @abstractmethod
    def delete_user(self, id_user: int) -> str:
        pass

    @abstractmethod
    def authenticate_user(self, email: str, password: str):
        pass
        