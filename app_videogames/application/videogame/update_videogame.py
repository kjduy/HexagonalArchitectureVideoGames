from ...domain.videogame import VideogameRepository
from ...infrastructure.sqlite.videogame import VideogameUpdateModel


class UpdateVideogame:

    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def update_videogame(self, videogame_id: int, videogame: VideogameUpdateModel) -> str:
        return self.videogame_repository.update_videogame(videogame_id, videogame)
        