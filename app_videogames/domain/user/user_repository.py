from abc import ABC, abstractmethod
from typing import Optional

from app_videogames.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, idUser: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, idUser: int):
        raise NotImplementedError
