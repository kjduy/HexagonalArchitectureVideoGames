from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    username: str = Field(example="Kevin123")
    email: str = Field(example="kevin.duy@ioet.com")
    password: str = Field(example="Myp@ssword123")

class UserUpdateModel(BaseModel):
    username: str = Field(example="Kevin124")
    password: str = Field(example="Changep@ssword124")
