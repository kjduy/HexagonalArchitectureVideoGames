from app_videogames.domain.user import UserRepository
from app_videogames.infrastructure.sqlite.user import UserUpdateModel


class UpdateUser:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def update_user(self, user_id: int, user: UserUpdateModel) -> str:
        return self.user_repository.update_user(user_id, user)
        