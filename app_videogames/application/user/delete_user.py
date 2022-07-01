from ...domain.user import UserRepository


class DeleteUser:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def delete_user(self, user_id: int) -> str:
        return self.user_repository.delete_user(user_id)
        