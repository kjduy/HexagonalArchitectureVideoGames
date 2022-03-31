from abc import abstractmethod

from .videogame import Videogame
from app_videogames.infrastructure.sqlite.videogame.videogame_create_model import VideogameCreateModel
from app_videogames.infrastructure.sqlite.videogame.videogame_update_model import VideogameUpdateModel


class VideogameRepository:

    @abstractmethod
    def get_videogames(self) -> Videogame:
        pass

    @abstractmethod
    def get_videogame_by_id(self, id_videogame: int) -> Videogame:
        pass

    @abstractmethod
    def insert_videogame(self, id_user: int, videogame: VideogameCreateModel) -> str:
        pass

    @abstractmethod
    def update_videogame(self, id_videogame: int, user: VideogameUpdateModel) -> str:
        pass

    @abstractmethod
    def delete_videogame(self, id_videogame: int) -> str:
        pass
        