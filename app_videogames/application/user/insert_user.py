from dependency_injector.wiring import inject

from ...domain.user import UserRepository
from ...infrastructure.sqlite.user import UserCreateModel


class InsertUser:

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def insert_user(self, user: UserCreateModel) -> str:
        return self.user_repository.insert_user(user)
        