from pydantic import BaseModel, Field


class UserUpdateModel(BaseModel):
    username: str = Field(example="Kevin124")
    password: str = Field(example="Changep@ssword124")
    