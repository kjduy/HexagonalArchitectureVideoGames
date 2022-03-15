import sqlite3
import functools
from abc import ABC, abstractmethod
from typing import Optional, cast

from app_videogames.domain.user import (
    User,
    EmailAlreadyExistsError,
    UserNotFoundError,
    UserRepository,
    Email,
    Password,
    Username
)

from .user_command_model import UserCreateModel, UserUpdateModel
from .user_query_model import UserReadModel


class UserCommandUseCaseUnitOfWork(ABC):
    user_repository: UserRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

class UserCommandUseCase(ABC):
    @abstractmethod
    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, idUser: int, data: UserUpdateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_user_by_id(self, idUser: int):
        raise NotImplementedError

class UserCommandUseCaseImpl(UserCommandUseCase):
    def __init__(
        self,
        uow: UserCommandUseCaseUnitOfWork,
    ):
        self.uow: UserCommandUseCaseUnitOfWork = uow

    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        connection = sqlite3.connect("./db/app_videogames.db")
        cursor = connection.cursor()
        try:
            numUsr = cursor.execute('SELECT count(*) FROM user').fetchone()
            if (numUsr[0] == 0):
                idUser = 0
            elif (numUsr[0] != 0):
                idUser = cursor.execute('select idUser from user order by idUser desc limit 1').fetchone()
                idUser = functools.reduce(lambda sub, ele: sub * 10 + ele, idUser)
            email = Email(data.email)
            password = Password(data.password)
            username = Username(data.username)
            user = User(idUser=idUser+1, username=username, email=email, password=password)
            existing_user = self.uow.user_repository.find_by_email(email.value)
            if existing_user is not None:
                raise EmailAlreadyExistsError
            self.uow.user_repository.create(user)
            self.uow.commit()
            created_user = self.uow.user_repository.find_by_id(idUser+1) 
        except:
            self.uow.rollback()
            raise
        return UserReadModel.from_entity(cast(User, created_user))

    def update_user(self, idUser: int, data: UserUpdateModel) -> Optional[UserReadModel]:
        try:
            existing_user = self.uow.user_repository.find_by_id(idUser)
            if existing_user is None:
                raise UserNotFoundError
            user = User(
                idUser=existing_user.idUser,
                username=Username(data.username),
                email=existing_user.email,
                password=Password(data.password),
            )
            self.uow.user_repository.update(user)
            updated_user = self.uow.user_repository.find_by_id(user.idUser)
            self.uow.commit()
        except:
            self.uow.rollback()
            raise
        return UserReadModel.from_entity(cast(User, updated_user))

    def delete_user_by_id(self, idUser: int):
        try:
            existing_user = self.uow.user_repository.find_by_id(idUser)
            if existing_user is None:
                raise UserNotFoundError
            self.uow.user_repository.delete_by_id(idUser)
            self.uow.commit()
        except:
            self.uow.rollback()
            raise
