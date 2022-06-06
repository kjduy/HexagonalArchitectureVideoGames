from pydantic import BaseModel, Field


class VideogameCreateModel(BaseModel):
    name: str = Field(example="Super Smash Bros Ultimate")
    price: float = Field(example=60.00)
    description: str = Field (
        example = "Is a fighting videogame developed " \
        "by Bandai Namco Entertainment and published by " \
        "Nintendo for the Nintendo Switch console"
    )
