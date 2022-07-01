from ...domain.level import LevelRepository
from ...infrastructure.sqlite.level import LevelCreateModel


class InsertLevel:

    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def insert_level(self, videogame_id: int, level: LevelCreateModel) -> str:
        return self.level_repository.insert_level(videogame_id, level)
        