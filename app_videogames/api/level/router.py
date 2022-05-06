import jwt

from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter, Depends, HTTPException, status

from app_videogames.api.level.level_container import LevelContainer
from app_videogames.application.level import (GetLevels, InsertLevel, UpdateLevel, DeleteLevel)
from app_videogames.infrastructure.sqlite.level import (LevelCreateModel, LevelUpdateModel)
from app_videogames.domain.level.value_object import (LevelNameError, DifficultyError, LastGameDateError)
from app_videogames.api.user.router import router, oauth2_scheme


@router.get('/levels')
@inject
async def get_levels(
    levels: GetLevels = Depends(Provide[LevelContainer.get_levels]),
    token: str = Depends(oauth2_scheme)
):
    return levels.get_levels()

@router.get('/level')
@inject
async def get_level_by_id(
    idLevel: int,
    level: GetLevels = Depends(Provide[LevelContainer.get_levels]),
    token: str = Depends(oauth2_scheme)
):
    return level.get_level_by_id(idLevel)

@router.post('/level')
@inject
async def insert_level(
    idVideogame: int,
    level_to_insert: LevelCreateModel,
    level: InsertLevel = Depends(Provide[LevelContainer.insert_level]),
):
    try:
        level_created = level.insert_level(idVideogame, level_to_insert)
    except LevelNameError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except DifficultyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except LastGameDateError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    return level_created

@router.put('/level')
@inject
async def update_level(
    idLevel: int,
    level_to_update: LevelUpdateModel,
    level: UpdateLevel = Depends(Provide[LevelContainer.update_level]),
    token: str = Depends(oauth2_scheme)
):
    try:
        level_updated = level.update_level(idLevel, level_to_update)
    except LevelNameError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except DifficultyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except LastGameDateError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    return level_updated

@router.delete('/level')
@inject
async def delete_level(
    idLevel: int,
    level: DeleteLevel = Depends(Provide[LevelContainer.delete_level]),
    token: str = Depends(oauth2_scheme)
):
    return level.delete_level(idLevel)
    