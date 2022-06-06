from dependency_injector.wiring import inject

from app_videogames.domain.videogame import VideogameRepository
from app_videogames.infrastructure.sqlite.videogame import VideogameCreateModel


class InsertVideogame:

    @inject
    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def insert_videogame(self, id_user: int, videogame: VideogameCreateModel) -> str:
        return self.videogame_repository.insert_videogame(id_user, videogame)
        