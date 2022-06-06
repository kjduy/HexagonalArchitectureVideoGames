from dependency_injector.wiring import inject

from app_videogames.domain.videogame import VideogameRepository
from app_videogames.infrastructure.sqlite.videogame import VideogameUpdateModel


class UpdateVideogame:

    @inject
    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def update_videogame(self, id_videogame: int, videogame: VideogameUpdateModel) -> str:
        return self.videogame_repository.update_videogame(id_videogame, videogame)
        