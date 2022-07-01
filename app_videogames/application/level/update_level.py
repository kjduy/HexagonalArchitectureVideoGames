from ...domain.level import LevelRepository
from ...infrastructure.sqlite.level import LevelUpdateModel


class UpdateLevel:

    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def update_level(self, level_id: int, level: LevelUpdateModel) -> str:
        return self.level_repository.update_level(level_id, level)
        