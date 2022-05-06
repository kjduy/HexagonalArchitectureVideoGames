from dependency_injector.wiring import inject

from app_videogames.domain.level import (Level, LevelRepository)


class GetLevels:

    @inject
    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def get_levels(self) -> Level:
        return self.level_repository.get_levels();

    def get_level_by_id(self, id_level: int) -> Level:
        return self.level_repository.get_level_by_id(id_level);
        