from app_videogames.domain.user import (User, UserRepository)


class GetUsers:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self) -> User:
        return self.user_repository.get_users()

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id)
        