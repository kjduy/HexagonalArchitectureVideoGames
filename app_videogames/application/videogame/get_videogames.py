from dependency_injector.wiring import inject

from app_videogames.domain.videogame import (Videogame, VideogameRepository)


class GetVideogames:

    @inject
    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def get_videogames(self) -> Videogame:
        return self.videogame_repository.get_videogames();

    def get_videogame_by_id(self, id_videogame: int) -> Videogame:
        return self.videogame_repository.get_videogame_by_id(id_videogame);
        