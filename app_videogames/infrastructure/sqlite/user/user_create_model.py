from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    username: str = Field(example='Kevin123')
    email: str = Field(example='test@test.com')
    password: str = Field(example='Myp@ssword123')
    