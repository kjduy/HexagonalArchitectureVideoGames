from pydantic import BaseModel, Field


class VideogameUpdateModel(BaseModel):
    name: str = Field(example="Super Smash Bros")
    price: float = Field(example=30.00)
    description: str = Field(example="Is a fighting videogame developed by Bandai Namco Entertainment and published by Nintendo for the Wii console")
