from app_videogames.domain.videogame.value_object import (
    VideogameName,
    Price,
    VideogameDescription
)


class Videogame:

    def __init__(
        self,
        id_videogame: int,
        name: VideogameName,
        price: Price,
        description: VideogameDescription,
        user_id: int
    ):
        self.id_videogame: int = id_videogame
        self.name: VideogameName = name
        self.price: Price = price
        self.description: VideogameDescription = description
        self.user_id: int = user_id
        