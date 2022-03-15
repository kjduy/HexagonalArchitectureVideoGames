from abc import ABC, abstractmethod
from typing import List, Optional

from .user_query_model import UserReadModel


class UserQueryService(ABC):
    @abstractmethod
    def find_by_id(self, idUser: int) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[UserReadModel]:
        raise NotImplementedError
