from app_videogames.domain.level import LevelRepository


class DeleteLevel:

    def __init__(self, level_repository: LevelRepository):
        self.level_repository = level_repository

    def delete_level(self, id_level: int) -> str:
        return self.level_repository.delete_level(id_level)
        