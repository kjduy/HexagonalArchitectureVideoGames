from ...domain.videogame import VideogameRepository
from ...infrastructure.sqlite.videogame import VideogameCreateModel


class InsertVideogame:

    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def insert_videogame(self, user_id: int, videogame: VideogameCreateModel) -> str:
        return self.videogame_repository.insert_videogame(user_id, videogame)
        