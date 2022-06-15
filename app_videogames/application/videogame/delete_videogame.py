from app_videogames.domain.videogame import VideogameRepository


class DeleteVideogame:

    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def delete_videogame(self, id_videogame: int) -> str:
        return self.videogame_repository.delete_videogame(id_videogame)
