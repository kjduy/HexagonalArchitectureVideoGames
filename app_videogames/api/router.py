from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Query, HTTPException, status


import logging
from typing import Iterator, List
from sqlalchemy.orm.session import Session

from app_videogames.domain.user import (
    UsersNotFoundError,
)
from app_videogames.infrastructure.sqlite.user import (
    UserQueryServiceImpl,
)
from app_videogames.infrastructure.sqlite.database import SessionLocal
from app_videogames.presentation.schema.user.user_error_message import (
    ErrorMessageUsersNotFound,
)
from app_videogames.usecase.user import (
    UserQueryService,
    UserQueryUseCase,
    UserQueryUseCaseImpl,
    UserReadModel,
)
from app_videogames.application.user.get_all import GetAllUsers
from app_videogames.container import Container

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get(
    "/users",
    response_model=List[UserReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageUsersNotFound,
        },
    },
)
@inject
async def get_users(
    user_query_usecase: GetAllUsers = Depends(Provide[Container.user_application_service]),
):
    try:
        users = user_query_usecase.get_users()
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