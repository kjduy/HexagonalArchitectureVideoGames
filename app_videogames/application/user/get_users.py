from dependency_injector.wiring import inject

from app_videogames.domain.user import (User, UserRepository)


class GetUsers:

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self) -> User:
        return self.user_repository.get_users()

    def get_user_by_id(self, id_user: int) -> User:
        return self.user_repository.get_user_by_id(id_user)
        