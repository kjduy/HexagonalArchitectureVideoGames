from ...domain.level import Level, LevelRepository


class GetLevels:

    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def get_levels(self) -> Level:
        return self.level_repository.get_levels()

    def get_level_by_id(self, level_id: int) -> Level:
        return self.level_repository.get_level_by_id(level_id)
        