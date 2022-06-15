from app_videogames.domain.level import LevelRepository
from app_videogames.infrastructure.sqlite.level import LevelCreateModel


class InsertLevel:

    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def insert_level(self, id_videogame: int, level: LevelCreateModel) -> str:
        return self.level_repository.insert_level(id_videogame, level)
        