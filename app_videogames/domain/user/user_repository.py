from abc import abstractmethod

from .user import User


class UserRepository:

    @abstractmethod
    def get_users(self) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def insert_user(self, data) -> str:
        pass

    @abstractmethod
    def update_user(self, user_id: int, data) -> str:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> str:
        pass

    @abstractmethod
    def authenticate_user(self, email: str, password: str):
        pass
        