from ...domain.videogame import Videogame, VideogameRepository


class GetVideogames:

    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def get_videogames(self) -> Videogame:
        return self.videogame_repository.get_videogames()

    def get_videogame_by_id(self, videogame_id: int) -> Videogame:
        return self.videogame_repository.get_videogame_by_id(videogame_id)
        