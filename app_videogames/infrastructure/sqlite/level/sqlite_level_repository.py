import sqlite3
import functools

from ....domain.level import Level, LevelRepository
from ....domain.level.value_object import LevelName, Difficulty, LastGameDate
from ..videogame import VideogameTable
from .. import session_com_rol_clo as crc, open_session
from .level_setup import LevelTable
from .level_create_model import LevelCreateModel
from .level_update_model import LevelUpdateModel


class SqliteLevelRepository(LevelRepository, open_session.SqliteRepository):

    def get_levels(self) -> Level:
        levels = self.session.query(LevelTable).all()
        open_session.SqliteRepository.close_session(self.session)
        return levels

    def get_level_by_id(self, level_id: int) -> str:
        level = self.session.query(LevelTable).filter_by(level_id=level_id).one()
        open_session.SqliteRepository.close_session(self.session)
        return level

    def insert_level(self, videogame_id: int, data: LevelCreateModel) -> str:
        connection = sqlite3.connect('./db/app_videogames.db')
        cursor = connection.cursor()
        num_lvl = cursor.execute('SELECT count(*) FROM level').fetchone()
        if num_lvl[0] == 0:
            level_id = 0
        elif num_lvl[0] != 0:
            level_id = cursor.execute (
                'select level_id from level order by level_id desc limit 1'
            ).fetchone()
            level_id = functools.reduce(lambda sub, ele: sub * 10 + ele, level_id)
        videogame = self.session.query(VideogameTable).filter_by(videogame_id=videogame_id).one()
        name = LevelName(data.name)
        difficulty = Difficulty(data.difficulty)
        last_game_date = LastGameDate(data.last_game_date)
        add_level = LevelTable(
            level_id = level_id+1,
            name = name.value,
            difficulty = difficulty.value,
            last_game_date = last_game_date.value,
            videogame_id = videogame.videogame_id)
        self.session.add(add_level)
        crc.session_commit_rollback_close(self.session)
        return 'Level created'

    def update_level(self, level_id: int, data: LevelUpdateModel) -> str:
        level = self.session.query(LevelTable).filter_by(level_id=level_id).one()
        name = LevelName(data.name)
        difficulty = Difficulty(data.difficulty)
        last_game_date = LastGameDate(data.last_game_date)
        level.name = name.value
        level.difficulty = difficulty.value
        level.last_game_date = last_game_date.value
        self.session.add(level)
        crc.session_commit_rollback_close(self.session)
        return 'Level updated'

    def delete_level(self, level_id: int) -> str:
        level = self.session.query(LevelTable).filter_by(level_id=level_id).one()
        self.session.delete(level)
        crc.session_commit_rollback_close(self.session)
        return 'Level deleted'
