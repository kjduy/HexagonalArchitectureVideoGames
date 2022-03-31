from dependency_injector import containers, providers

from app_videogames.infrastructure.sqlite.videogame.sqlite_videogame_repository import SqliteVideogameRepository
from app_videogames.application.videogame import (GetVideogames, InsertVideogame, UpdateVideogame, DeleteVideogame)


class VideogameContainer(containers.DeclarativeContainer):
    
    sqlite_videogame_repository = providers.Singleton(SqliteVideogameRepository)

    get_videogames = providers.Factory(
        GetVideogames,
        videogame_repository = sqlite_videogame_repository,
    )

    insert_videogame = providers.Factory(
        InsertVideogame,
        videogame_repository = sqlite_videogame_repository,
    )

    update_videogame = providers.Factory(
        UpdateVideogame,
        videogame_repository = sqlite_videogame_repository,
    )
    
    delete_videogame = providers.Factory(
        DeleteVideogame,
        videogame_repository = sqlite_videogame_repository,
    )
