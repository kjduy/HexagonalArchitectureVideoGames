import jwt

from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, HTTPException, status

from app_videogames.application.user import (GetUsers, InsertUser, UpdateUser, DeleteUser, AuthenticateUser)
from app_videogames.api.user.user_container import UserContainer
from app_videogames.infrastructure.sqlite.user import (UserCreateModel, UserUpdateModel)
from app_videogames.domain.user.value_object import (EmailError, PasswordError, UsernameError)

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

JWT_SECRET = 'myjwtsecret'

@router.post('/login')
@inject
async def generate_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user: AuthenticateUser = Depends(Provide[UserContainer.authenticate_user]),
):
    user = user.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Invalid username or password'
        )
    token = jwt.encode(user, JWT_SECRET)
    return token

@router.get('/users')
@inject
async def get_users(
    users: GetUsers = Depends(Provide[UserContainer.get_users]),
    token: str = Depends(oauth2_scheme)
):
    return users.get_users()

@router.get('/user')
@inject
async def get_user_by_id(
    idUser: int,
    user: GetUsers = Depends(Provide[UserContainer.get_users]),
    token: str = Depends(oauth2_scheme)
):
    return user.get_user_by_id(idUser)

@router.post('/user')
@inject
async def insert_user(
    user_to_insert: UserCreateModel,
    user: InsertUser = Depends(Provide[UserContainer.insert_user]),
    token: str = Depends(oauth2_scheme)
):
    try:
        user_created = user.insert_user(user_to_insert)
    except EmailError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except PasswordError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except UsernameError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    return user_created

@router.put('/user')
@inject
async def update_user(
    idUser: int,
    user_to_update: UserUpdateModel,
    user: UpdateUser = Depends(Provide[UserContainer.update_user]),
    token: str = Depends(oauth2_scheme)
):
    try:
        user_updated = user.update_user(idUser, user_to_update)
    except PasswordError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except UsernameError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    return user_updated

@router.delete('/user')
@inject
async def delete_user(
    idUser: int,
    user: DeleteUser = Depends(Provide[UserContainer.delete_user]),
    token: str = Depends(oauth2_scheme)
):
    return user.delete_user(idUser)
    