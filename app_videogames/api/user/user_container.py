from dependency_injector import containers, providers

from app_videogames.infrastructure.sqlite.user.sqlite_user_repository import SqliteUserRepository
from app_videogames.application.user import (GetUsers, InsertUser, UpdateUser, DeleteUser, AuthenticateUser)


class UserContainer(containers.DeclarativeContainer):
    
    sqlite_user_repository = providers.Singleton(SqliteUserRepository)

    get_users = providers.Factory(
        GetUsers,
        user_repository = sqlite_user_repository,
    )

    insert_user = providers.Factory(
        InsertUser,
        user_repository = sqlite_user_repository,
    )

    update_user = providers.Factory(
        UpdateUser,
        user_repository = sqlite_user_repository,
    )
    
    delete_user = providers.Factory(
        DeleteUser,
        user_repository = sqlite_user_repository,
    )

    authenticate_user = providers.Factory(
        AuthenticateUser,
        user_repository = sqlite_user_repository,
    )
