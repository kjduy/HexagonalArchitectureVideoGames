import jwt

from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .user_container import (
    GetUsers,
    UserContainer,
    InsertUser,
    UpdateUser,
    DeleteUser,
    AuthenticateUser
)
from ...sqlite.user import UserCreateModel, UserUpdateModel
from ....domain.user.value_object import EmailError, PasswordError, UsernameError


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
    _token = jwt.encode(user, JWT_SECRET)
    return _token

@router.get('/users')
@inject
async def get_users(
    users: GetUsers = Depends(Provide[UserContainer.get_users]),
    _token: str = Depends(oauth2_scheme)
):
    return users.get_users()

@router.get('/user')
@inject
async def get_user_by_id(
    user_id: int,
    user: GetUsers = Depends(Provide[UserContainer.get_users]),
    _token: str = Depends(oauth2_scheme)
):
    return user.get_user_by_id(user_id)

@router.post('/user')
@inject
async def insert_user(
    user_to_insert: UserCreateModel,
    user: InsertUser = Depends(Provide[UserContainer.insert_user]),
):
    try:
        user_created = user.insert_user(user_to_insert)
    except EmailError as error:
        raise HTTPException (
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except PasswordError as error:
        raise HTTPException (
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except UsernameError as error:
        raise HTTPException (
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    return user_created

@router.put('/user')
@inject
async def update_user(
    user_id: int,
    user_to_update: UserUpdateModel,
    user: UpdateUser = Depends(Provide[UserContainer.update_user]),
    _token: str = Depends(oauth2_scheme)
):
    try:
        user_updated = user.update_user(user_id, user_to_update)
    except PasswordError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except UsernameError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    return user_updated

@router.delete('/user')
@inject
async def delete_user(
    user_id: int,
    user: DeleteUser = Depends(Provide[UserContainer.delete_user]),
    _token: str = Depends(oauth2_scheme)
):
    return user.delete_user(user_id)
    