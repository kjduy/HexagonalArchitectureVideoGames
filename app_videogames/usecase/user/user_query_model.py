from pydantic import BaseModel, Field

from app_videogames.domain.user import User


class UserReadModel(BaseModel):
    idUser: int = Field(example="1")
    username: str = Field(example="Kevin123")
    email: str = Field(example="kevin.duy@ioet.com")
    password: str = Field(example="Myp@ssword123")

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(user: User) -> "UserReadModel":
        return UserReadModel(
            idUser=user.idUser,
            username=user.username.value,
            email=user.email.value,
            password=user.password.value,
        )
