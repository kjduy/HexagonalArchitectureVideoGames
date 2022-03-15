from typing import Union

from sqlalchemy import Column, Integer, String

from app_videogames.domain.user import Email, Password, User, Username
from app_videogames.infrastructure.sqlite.database import Base
from app_videogames.usecase.user import UserReadModel


class UserDTO(Base):
    __tablename__ = "user"
    idUser: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    username: Union[str, Column] = Column(String, nullable=False)
    email: Union[str, Column] = Column(String, unique=True, nullable=False)
    password: Union[int, Column] = Column(String, nullable=False)

    def to_entity(self) -> User:
        return User(
            idUser=self.idUser,
            username=Username(self.username),
            email=Email(self.email),
            password=Password(self.password),
        )

    def to_read_model(self) -> UserReadModel:
        return UserReadModel(
            idUser=self.idUser,
            username=self.username,
            email=self.email,
            password=self.password,
        )

    @staticmethod
    def from_entity(user: User) -> "UserDTO":
        return UserDTO(
            idUser=user.idUser,
            username=user.username.value,
            email=user.email.value,
            password=user.password.value,
        )
