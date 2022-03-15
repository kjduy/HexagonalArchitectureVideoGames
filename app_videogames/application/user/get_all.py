from dependency_injector.wiring import inject

from app_videogames.domain.user import User
from typing import Iterator, List

from app_videogames.usecase.user import (
    UserQueryService,
    UserQueryUseCase,
    UserQueryUseCaseImpl,
    UserReadModel,
)

from app_videogames.domain.user import (
    UserRepository
)

class GetAllUsers:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self) -> List[UserReadModel]:
        return self.user_repository.find_all()