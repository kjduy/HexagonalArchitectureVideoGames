from ...domain.level import LevelRepository


class DeleteLevel:

    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def delete_level(self, level_id: int) -> str:
        return self.level_repository.delete_level(level_id)
