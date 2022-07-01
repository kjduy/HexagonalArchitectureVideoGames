from abc import abstractmethod, ABC

from . import Videogame


# pylint: disable=duplicate-code
class VideogameRepository(ABC):

    @abstractmethod
    def get_videogames(self) -> Videogame:
        pass

    @abstractmethod
    def get_videogame_by_id(self, videogame_id: int) -> Videogame:
        pass

    @abstractmethod
    def insert_videogame(self, user_id: int, data) -> str:
        pass

    @abstractmethod
    def update_videogame(self, videogame_id: int, data) -> str:
        pass

    @abstractmethod
    def delete_videogame(self, videogame_id: int) -> str:
        pass
