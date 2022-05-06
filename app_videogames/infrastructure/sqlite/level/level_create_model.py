from pydantic import BaseModel, Field


class LevelCreateModel(BaseModel):
    name: str = Field(example="First Level")
    difficulty: str = Field(example="Easy")
    last_game_date: str = Field(example="2022-04-28")
