import sqlite3
import functools

from ....domain.videogame import Videogame, VideogameRepository
from ....domain.videogame.value_object import (
    VideogameName,
    Price,
    VideogameDescription
)
from ..user import UserTable
from .. import session_com_rol_clo as crc, open_session
from .videogame_setup import VideogameTable
from .videogame_create_model import VideogameCreateModel
from .videogame_update_model import VideogameUpdateModel


class SqliteVideogameRepository(VideogameRepository, open_session.SqliteRepository):

    def get_videogames(self) -> Videogame:
        videogames = self.session.query(VideogameTable).all()
        open_session.SqliteRepository.close_session(self.session)
        return videogames

    def get_videogame_by_id(self, videogame_id: int) -> str:
        videogame = self.session.query(VideogameTable).filter_by(videogame_id=videogame_id).one()
        open_session.SqliteRepository.close_session(self.session)
        return videogame

    def insert_videogame(self, user_id: int, data: VideogameCreateModel) -> str:
        connection = sqlite3.connect('./db/app_videogames.db')
        cursor = connection.cursor()
        num_vdg = cursor.execute('SELECT count(*) FROM videogame').fetchone()
        if num_vdg[0] == 0:
            videogame_id = 0
        elif num_vdg[0] != 0:
            videogame_id = cursor.execute (
                'select videogame_id from videogame order by videogame_id desc limit 1'
            ).fetchone()
            videogame_id = functools.reduce(lambda sub, ele: sub * 10 + ele, videogame_id)
        user = self.session.query(UserTable).filter_by(user_id=user_id).one()
        name = VideogameName(data.name)
        price = Price(data.price)
        description = VideogameDescription(data.description)
        add_videogame = VideogameTable(
            videogame_id = videogame_id+1,
            name = name.value,
            price = price.value,
            description = description.value,
            user_id = user.user_id)
        self.session.add(add_videogame)
        crc.session_commit_rollback_close(self.session)
        return 'Videogame created'

    def update_videogame(self, videogame_id: int, data: VideogameUpdateModel) -> str:
        videogame = self.session.query(VideogameTable).filter_by(videogame_id=videogame_id).one()
        name = VideogameName(data.name)
        price = Price(data.price)
        description = VideogameDescription(data.description)
        videogame.name = name.value
        videogame.price = price.value
        videogame.description = description.value
        self.session.add(videogame)
        crc.session_commit_rollback_close(self.session)
        return 'Videogame updated'

    def delete_videogame(self, videogame_id: int) -> str:
        videogame = self.session.query(VideogameTable).filter_by(videogame_id=videogame_id).one()
        self.session.delete(videogame)
        crc.session_commit_rollback_close(self.session)
        return 'Videogame deleted'
