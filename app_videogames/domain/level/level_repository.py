from abc import abstractmethod

from .level import Level


class LevelRepository:

    @abstractmethod
    def get_levels(self) -> Level:
        pass

    @abstractmethod
    def get_level_by_id(self, id_level: int) -> Level:
        pass

    @abstractmethod
    def insert_level(self, id_videogame: int, data) -> str:
        pass

    @abstractmethod
    def update_level(self, id_level: int, data) -> str:
        pass

    @abstractmethod
    def delete_level(self, id_level: int) -> str:
        pass
        