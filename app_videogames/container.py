from dependency_injector import containers, providers

from app_videogames.usecase.user import (
    UserQueryService,
    UserQueryUseCase,
    UserQueryUseCaseImpl,
    UserReadModel,
)

from typing import Iterator, List
from sqlalchemy.orm.session import Session
from fastapi import APIRouter, Depends, Query, HTTPException, status
from app_videogames.application.user.get_all import GetAllUsers

class Container(containers.DeclarativeContainer):
    def get_session() -> Iterator[Session]:
        session: Session = SessionLocal()
        try:
            yield session
        finally:
            session.close()

    def user_query_usecase(session: Session = Depends(get_session)) -> UserQueryUseCase:
        user_query_service: UserQueryService = UserQueryServiceImpl(session)
        return UserQueryUseCaseImpl(user_query_service)
    
    user_repository = user_query_usecase

    user_application_service = providers.Factory(
        GetAllUsers,
        user_repository=user_repository,
    )
