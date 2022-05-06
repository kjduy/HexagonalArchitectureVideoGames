from pydantic import BaseModel, Field


class LevelUpdateModel(BaseModel):
    name: str = Field(example="Another Level")
    difficulty: str = Field(example='Medium')
    last_game_date: str = Field(example="2022-04-29")
