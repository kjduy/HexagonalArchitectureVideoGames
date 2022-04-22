import jwt

from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, HTTPException, status

from app_videogames.api.videogame.videogame_container import VideogameContainer
from app_videogames.application.videogame import (GetVideogames, InsertVideogame, UpdateVideogame, DeleteVideogame)
from app_videogames.infrastructure.sqlite.videogame import (VideogameCreateModel, VideogameUpdateModel)
from app_videogames.domain.videogame.value_object import (VideogameNameError, PriceError, VideogameDescriptionError)
from app_videogames.api.user.router import router, oauth2_scheme


@router.get('/videogames')
@inject
async def get_videogames(
    videogames: GetVideogames = Depends(Provide[VideogameContainer.get_videogames]),
    token: str = Depends(oauth2_scheme)
):
    return videogames.get_videogames()

@router.get('/videogame')
@inject
async def get_videogame_by_id(
    idVideogame: int,
    videogame: GetVideogames = Depends(Provide[VideogameContainer.get_videogames]),
    token: str = Depends(oauth2_scheme)
):
    return videogame.get_videogame_by_id(idVideogame)

@router.post('/videogame')
@inject
async def insert_videogame(
    idUser: int,
    videogame_to_insert: VideogameCreateModel,
    videogame: InsertVideogame = Depends(Provide[VideogameContainer.insert_videogame]),
    token: str = Depends(oauth2_scheme)
):
    try:
        videogame_created = videogame.insert_videogame(idUser, videogame_to_insert)
    except VideogameNameError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except PriceError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except VideogameDescriptionError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    return videogame_created

@router.put('/videogame')
@inject
async def update_videogame(
    idVideogame: int,
    videogame_to_update: VideogameUpdateModel,
    videogame: UpdateVideogame = Depends(Provide[VideogameContainer.update_videogame]),
    token: str = Depends(oauth2_scheme)
):
    try:
        videogame_updated = videogame.update_videogame(idVideogame, videogame_to_update)
    except VideogameNameError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except PriceError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except VideogameDescriptionError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    return videogame_updated

@router.delete('/videogame')
@inject
async def delete_videogame(
    idVideogame: int,
    videogame: DeleteVideogame = Depends(Provide[VideogameContainer.delete_videogame]),
    token: str = Depends(oauth2_scheme)
):
    return videogame.delete_videogame(idVideogame)
    