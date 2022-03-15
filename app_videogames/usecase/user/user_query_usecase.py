from abc import ABC, abstractmethod
from typing import List, Optional

from app_videogames.domain.user import UserNotFoundError, UsersNotFoundError

from .user_query_model import UserReadModel
from .user_query_service import UserQueryService


class UserQueryUseCase(ABC):
    @abstractmethod
    def fetch_user_by_id(self, idUser: int) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_users(self) -> List[UserReadModel]:
        raise NotImplementedError

class UserQueryUseCaseImpl(UserQueryUseCase):
    def __init__(self, user_query_service: UserQueryService):
        self.user_query_service: UserQueryService = user_query_service

    def fetch_user_by_id(self, idUser: int) -> Optional[UserReadModel]:
        try:
            user = self.user_query_service.find_by_id(idUser)
            if user is None:
                raise UserNotFoundError
        except:
            raise
        return user

    def fetch_users(self) -> List[UserReadModel]:
        try:
            users = self.user_query_service.find_all()
            if users is None:
                raise UsersNotFoundError
        except:
            raise
        return users
