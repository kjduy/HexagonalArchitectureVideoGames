from app_videogames.domain.level import LevelRepository
from app_videogames.infrastructure.sqlite.level import LevelUpdateModel


class UpdateLevel:

    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def update_level(self, id_level: int, level: LevelUpdateModel) -> str:
        return self.level_repository.update_level(id_level, level)
        