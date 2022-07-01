from dependency_injector.wiring import inject, Provide

from fastapi import Depends, HTTPException, status

from .level_container import LevelContainer
from ....application.level import GetLevels, InsertLevel, UpdateLevel, DeleteLevel
from ...sqlite.level import LevelCreateModel, LevelUpdateModel
from ....domain.level.value_object import (
    LevelNameError,
    DifficultyError,
    LastGameDateError
)
from ..user.router import router, oauth2_scheme


@router.get('/levels')
@inject
async def get_levels(
    levels: GetLevels = Depends(Provide[LevelContainer.get_levels]),
    _token: str = Depends(oauth2_scheme)
):
    return levels.get_levels()

@router.get('/level')
@inject
async def get_level_by_id(
    level_id: int,
    level: GetLevels = Depends(Provide[LevelContainer.get_levels]),
    _token: str = Depends(oauth2_scheme)
):
    return level.get_level_by_id(level_id)

@router.post('/level')
@inject
async def insert_level(
    videogame_id: int,
    level_to_insert: LevelCreateModel,
    level: InsertLevel = Depends(Provide[LevelContainer.insert_level]),
    _token: str = Depends(oauth2_scheme)
):
    try:
        level_created = level.insert_level(videogame_id, level_to_insert)
    except LevelNameError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except DifficultyError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except LastGameDateError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    return level_created

@router.put('/level')
@inject
async def update_level(
    level_id: int,
    level_to_update: LevelUpdateModel,
    level: UpdateLevel = Depends(Provide[LevelContainer.update_level]),
    _token: str = Depends(oauth2_scheme)
):
    try:
        level_updated = level.update_level(level_id, level_to_update)
    except LevelNameError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except DifficultyError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    except LastGameDateError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error.message,
        ) from error
    return level_updated

@router.delete('/level')
@inject
async def delete_level(
    level_id: int,
    level: DeleteLevel = Depends(Provide[LevelContainer.delete_level]),
    _token: str = Depends(oauth2_scheme)
):
    return level.delete_level(level_id)
    