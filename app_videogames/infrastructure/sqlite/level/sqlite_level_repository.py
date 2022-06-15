import sqlite3
import functools

from app_videogames.domain.level import (Level, LevelRepository)
from app_videogames.domain.level.value_object import (LevelName, Difficulty, LastGameDate)
from app_videogames.infrastructure.sqlite.videogame import VideogameTable
from app_videogames.infrastructure.sqlite import session_com_rol_clo as crc, open_session
from .level_setup import LevelTable
from .level_create_model import LevelCreateModel
from .level_update_model import LevelUpdateModel


engine = create_engine('sqlite:///./db/app_videogames.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class SqliteLevelRepository(LevelRepository):

    def get_levels(self) -> Level:
        session = open_session.create_session()
        levels = session.query(LevelTable).all()
        return levels

    def get_level_by_id(self, id_level: int) -> str:
        session = open_session.create_session()
        level = session.query(LevelTable).filter_by(idLevel=id_level).one()
        return level

    def insert_level(self, id_videogame: int, data: LevelCreateModel) -> str:
        session = open_session.create_session()
        connection = sqlite3.connect("./db/app_videogames.db")
        cursor = connection.cursor()
        num_lvl = cursor.execute('SELECT count(*) FROM level').fetchone()
        if num_lvl[0] == 0:
            id_level = 0
        elif num_lvl[0] != 0:
            id_level = cursor.execute (
                'select idLevel from level order by idLevel desc limit 1'
            ).fetchone()
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
        crc.session_commit_rollback_close(session)
        return "Level created"

    def update_level(self, id_level: int, data: LevelUpdateModel) -> str:
        session = open_session.create_session()
        level = session.query(LevelTable).filter_by(idLevel=id_level).one()
        name = LevelName(data.name)
        difficulty = Difficulty(data.difficulty)
        last_game_date = LastGameDate(data.last_game_date)
        level.name = name.value
        level.difficulty = difficulty.value
        level.last_game_date = last_game_date.value
        session.add(level)
        crc.session_commit_rollback_close(session)
        return "Level updated"

    def delete_level(self, id_level: int) -> str:
        session = open_session.create_session()
        level = session.query(LevelTable).filter_by(idLevel=id_level).one()
        session.delete(level)
        crc.session_commit_rollback_close(session)
        return "Level deleted"
