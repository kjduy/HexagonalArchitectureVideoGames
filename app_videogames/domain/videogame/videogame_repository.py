from abc import abstractmethod

from .videogame import Videogame


class VideogameRepository:

    @abstractmethod
    def get_videogames(self) -> Videogame:
        pass

    @abstractmethod
    def get_videogame_by_id(self, id_videogame: int) -> Videogame:
        pass

    @abstractmethod
    def insert_videogame(self, id_user: int, data) -> str:
        pass

    @abstractmethod
    def update_videogame(self, id_videogame: int, data) -> str:
        pass

    @abstractmethod
    def delete_videogame(self, id_videogame: int) -> str:
        pass
        