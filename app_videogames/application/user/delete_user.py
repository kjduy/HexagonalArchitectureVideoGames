from dependency_injector.wiring import inject

from app_videogames.domain.user import UserRepository


class DeleteUser:

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def delete_user(self, id_user: int) -> str:
        return self.user_repository.delete_user(id_user);
        