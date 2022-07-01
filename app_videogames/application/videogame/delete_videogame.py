from ...domain.videogame import VideogameRepository


class DeleteVideogame:

    def __init__(self, videogame_repository: VideogameRepository):
        self.videogame_repository = videogame_repository

    def delete_videogame(self, videogame_id: int) -> str:
        return self.videogame_repository.delete_videogame(videogame_id)
