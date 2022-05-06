import sqlite3
import functools

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_videogames.domain.level import (Level, LevelRepository)
from app_videogames.domain.level.value_object import (LevelName, Difficulty, LastGameDate)
from app_videogames.infrastructure.sqlite.videogame import VideogameTable
from .level_setup import LevelTable
from .level_create_model import LevelCreateModel
from .level_update_model import LevelUpdateModel


engine = create_engine('sqlite:///./db/app_videogames.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class SqliteLevelRepository(LevelRepository):
    
    def get_levels(self) -> Level:
        levels = session.query(LevelTable).all()
        return levels

    def get_level_by_id(self, id_lvel: int) -> str:
        level = session.query(LevelTable).filter_by(idLevel=id_level).one()
        return level

    def insert_level(self, id_videogame: int, data: LevelCreateModel) -> str:
        connection = sqlite3.connect("./db/app_videogames.db")
        cursor = connection.cursor()
        numLvl = cursor.execute('SELECT count(*) FROM level').fetchone()
        if (numLvl[0] == 0):
            id_level = 0
        elif (numLvl[0] != 0):
            id_level = cursor.execute('select idLevel from level order by idLevel desc limit 1').fetchone()
            id_level = functools.reduce(lambda sub, ele: sub * 10 + ele, id_level)
        videogame = session.query(VideogameTable).filter_by(idVideogame=id_videogame).one()
        name = LevelName(data.name)
        difficulty = Difficulty(data.difficulty)
        last_game_date = LastGameDate(data.last_game_date)
        add_level = LevelTable(
            idLevel = id_level+1,
            name = name.value,
            difficulty = difficulty.value,
            last_game_date = last_game_date.value,
            idVideogame = videogame.idVideogame)
        session.add(add_level)
        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return "Level created"
        
    def update_level(self, id_level: int, data: LevelUpdateModel) -> str:
        level = session.query(LevelTable).filter_by(idLevel=id_level).one()
        name = LevelName(data.name)
        difficulty = Difficulty(data.difficulty)
        last_game_date = LastGameDate(data.last_game_date)
        level.name = name.value
        level.difficulty = difficulty.value
        level.last_game_date = last_game_date.value
        session.add(level)
        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return "Level updated"

    def delete_level(self, id_level: int) -> str:
        level = session.query(LevelTable).filter_by(idLevel=id_level).one()
        session.delete(level)
        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return "Level deleted"
