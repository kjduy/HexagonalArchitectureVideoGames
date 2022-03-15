from pydantic import BaseModel, Field

from app_videogames.domain.user import (
    EmailAlreadyExistsError,
    UserNotFoundError,
    UsersNotFoundError,
)


class ErrorMessageUserNotFound(BaseModel):
    detail: str = Field(example=UserNotFoundError.message)

class ErrorMessageUsersNotFound(BaseModel):
    detail: str = Field(example=UsersNotFoundError.message)

class ErrorMessageEmailAlreadyExists(BaseModel):
    detail: str = Field(example=EmailAlreadyExistsError.message)
