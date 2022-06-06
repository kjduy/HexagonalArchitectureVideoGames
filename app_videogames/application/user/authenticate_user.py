from dependency_injector.wiring import inject

from app_videogames.domain.user import UserRepository


class AuthenticateUser:

    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str):
        return self.user_repository.authenticate_user(email, password)
        