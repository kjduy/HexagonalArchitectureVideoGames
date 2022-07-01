from abc import abstractmethod, ABC

from . import Level


# pylint: disable=duplicate-code
class LevelRepository(ABC):

    @abstractmethod
    def get_levels(self) -> Level:
        pass

    @abstractmethod
    def get_level_by_id(self, level_id: int) -> Level:
        pass

    @abstractmethod
    def insert_level(self, videogame_id: int, data) -> str:
        pass

    @abstractmethod
    def update_level(self, level_id: int, data) -> str:
        pass

    @abstractmethod
    def delete_level(self, level_id: int) -> str:
        pass
