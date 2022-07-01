from dependency_injector import containers, providers

from ...sqlite.level.sqlite_level_repository import SqliteLevelRepository
from ....application.level import GetLevels, InsertLevel, UpdateLevel, DeleteLevel


class LevelContainer(containers.DeclarativeContainer):
    sqlite_level_repository = providers.Singleton(SqliteLevelRepository)

    get_levels = providers.Factory(
        GetLevels,
        level_repository = sqlite_level_repository,
    )

    insert_level = providers.Factory(
        InsertLevel,
        level_repository = sqlite_level_repository,
    )

    update_level = providers.Factory(
        UpdateLevel,
        level_repository = sqlite_level_repository,
    )

    delete_level = providers.Factory(
        DeleteLevel,
        level_repository = sqlite_level_repository,
    )
