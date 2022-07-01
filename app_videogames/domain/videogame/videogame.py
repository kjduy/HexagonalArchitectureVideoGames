from .value_object import (
    VideogameName,
    Price,
    VideogameDescription
)


class Videogame:

    videogame_id: int
    name: VideogameName
    price: Price
    description: VideogameDescription
    user_id: int

    def __init__(
        self,
        videogame_id: int,
        name: VideogameName,
        price: Price,
        description: VideogameDescription,
        user_id: int
    ):
        self.videogame_id: int = videogame_id
        self.name: VideogameName = name
        self.price: Price = price
        self.description: VideogameDescription = description
        self.user_id: int = user_id
