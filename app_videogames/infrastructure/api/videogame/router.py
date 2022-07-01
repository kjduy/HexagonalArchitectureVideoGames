from dependency_injector.wiring import inject, Provide

from fastapi import Depends, HTTPException, status

from .videogame_container import (
    VideogameContainer,
    GetVideogames,
    InsertVideogame,
    UpdateVideogame,
    DeleteVideogame
)
from ...sqlite.videogame import (
    VideogameCreateModel,
    VideogameUpdateModel
)
from ....domain.videogame.value_object import (
    VideogameNameError,
    PriceError,
    VideogameDescriptionError
)
from ..user.router import router, oauth2_scheme


@router.get('/videogames')
@inject
async def get_videogames(
    videogames: GetVideogames = Depends(Provide[VideogameContainer.get_videogames]),
    _token: str = Depends(oauth2_scheme)
):
    return videogames.get_videogames()

@router.get('/videogame')
@inject
async def get_videogame_by_id(
    videogame_id: int,
    videogame: GetVideogames = Depends(Provide[VideogameContainer.get_videogames]),
    _token: str = Depends(oauth2_scheme)
):
    return videogame.get_videogame_by_id(videogame_id)

@router.post('/videogame')
@inject
async def insert_videogame(
    user_id: int,
    videogame_to_insert: VideogameCreateModel,
    videogame: InsertVideogame = Depends(Provide[VideogameContainer.insert_videogame]),
    _token: str = Depends(oauth2_scheme)
):
    try:
        videogame_created = videogame.insert_videogame(user_id, videogame_to_insert)
    except VideogameNameError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except PriceError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except VideogameDescriptionError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    return videogame_created

@router.put('/videogame')
@inject
async def update_videogame(
    videogame_id: int,
    videogame_to_update: VideogameUpdateModel,
    videogame: UpdateVideogame = Depends(Provide[VideogameContainer.update_videogame]),
    _token: str = Depends(oauth2_scheme)
):
    try:
        videogame_updated = videogame.update_videogame(videogame_id, videogame_to_update)
    except VideogameNameError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except PriceError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except VideogameDescriptionError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    return videogame_updated

@router.delete('/videogame')
@inject
async def delete_videogame(
    videogame_id: int,
    videogame: DeleteVideogame = Depends(Provide[VideogameContainer.delete_videogame]),
    _token: str = Depends(oauth2_scheme)
):
    return videogame.delete_videogame(videogame_id)
    