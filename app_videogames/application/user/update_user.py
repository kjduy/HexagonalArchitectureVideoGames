from dependency_injector.wiring import inject

from app_videogames.domain.user import UserRepository
from app_videogames.infrastructure.sqlite.user import UserUpdateModel


class UpdateUser:

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def update_user(self, id_user: int, user: UserUpdateModel) -> str:
        return self.user_repository.update_user(id_user, user)
        