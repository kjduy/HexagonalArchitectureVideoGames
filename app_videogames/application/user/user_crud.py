import logging
from typing import Iterator, List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm.session import Session

from app_videogames.domain.user import (
    EmailAlreadyExistsError,
    UserNotFoundError,
    UserRepository,
    UsersNotFoundError,
)
from app_videogames.infrastructure.sqlite.user import (
    UserCommandUseCaseUnitOfWorkImpl,
    UserQueryServiceImpl,
    UserRepositoryImpl,
)
from app_videogames.infrastructure.sqlite.database import SessionLocal, create_tables
from app_videogames.presentation.schema.user.user_error_message import (
    ErrorMessageEmailAlreadyExists,
    ErrorMessageUserNotFound,
    ErrorMessageUsersNotFound,
)
from app_videogames.usecase.user import (
    UserCommandUseCase,
    UserCommandUseCaseImpl,
    UserCommandUseCaseUnitOfWork,
    UserCreateModel,
    UserQueryService,
    UserQueryUseCase,
    UserQueryUseCaseImpl,
    UserReadModel,
    UserUpdateModel,
)


logger = logging.getLogger(__name__)

app = FastAPI()

create_tables()

class UserCRUD:
    def get_session() -> Iterator[Session]:
        session: Session = SessionLocal()
        try:
            yield session
        finally:
            session.close()

    def user_query_usecase(session: Session = Depends(get_session)) -> UserQueryUseCase:
        user_query_service: UserQueryService = UserQueryServiceImpl(session)
        return UserQueryUseCaseImpl(user_query_service)

    def user_command_usecase(session: Session = Depends(get_session)) -> UserCommandUseCase:
        user_repository: UserRepository = UserRepositoryImpl(session)
        uow: UserCommandUseCaseUnitOfWork = UserCommandUseCaseUnitOfWorkImpl(
            session, user_repository=user_repository
        )
        return UserCommandUseCaseImpl(uow)

    @app.post(
        "/users",
        response_model=UserReadModel,
        status_code=status.HTTP_201_CREATED,
        responses={
            status.HTTP_409_CONFLICT: {
                "model": ErrorMessageEmailAlreadyExists,
            },
        },
    )
    async def create_user(
        data: UserCreateModel,
        user_command_usecase: UserCommandUseCase = Depends(user_command_usecase),
    ):
        try:
            user = user_command_usecase.create_user(data)
        except EmailAlreadyExistsError as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=e.message,
            )
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return user

    @app.get(
        "/users",
        response_model=List[UserReadModel],
        status_code=status.HTTP_200_OK,
        responses={
            status.HTTP_404_NOT_FOUND: {
                "model": ErrorMessageUsersNotFound,
            },
        },
    )
    async def get_users(
        user_query_usecase: UserQueryUseCase = Depends(user_query_usecase),
    ):
        try:
            users = user_query_usecase.fetch_users()
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        if len(users) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=UsersNotFoundError.message,
            )
        return users

    @app.get(
        "/users/{user_id}",
        response_model=UserReadModel,
        status_code=status.HTTP_200_OK,
        responses={
            status.HTTP_404_NOT_FOUND: {
                "model": ErrorMessageUserNotFound,
            },
        },
    )
    async def get_user(
        user_id: int,
        user_query_usecase: UserQueryUseCase = Depends(user_query_usecase),
    ):
        try:
            user = user_query_usecase.fetch_user_by_id(user_id)
        except UserNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=e.message,
            )
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return user

    @app.put(
        "/users/{user_id}",
        response_model=UserReadModel,
        status_code=status.HTTP_202_ACCEPTED,
        responses={
            status.HTTP_404_NOT_FOUND: {
                "model": ErrorMessageUserNotFound,
            },
        },
    )
    async def update_user(
        user_id: int,
        data: UserUpdateModel,
        user_command_usecase: UserCommandUseCase = Depends(user_command_usecase),
    ):
        try:
            updated_user = user_command_usecase.update_user(user_id, data)
        except UserNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=e.message,
            )
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return updated_user

    @app.delete(
        "/users/{user_id}",
        status_code=status.HTTP_202_ACCEPTED,
        responses={
            status.HTTP_404_NOT_FOUND: {
                "model": ErrorMessageUserNotFound,
            },
        },
    )
    async def delete_user(
        user_id: int,
        user_command_usecase: UserCommandUseCase = Depends(user_command_usecase),
    ):
        try:
            user_command_usecase.delete_user_by_id(user_id)
        except UserNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=e.message,
            )
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return "Successfully deleted user"
