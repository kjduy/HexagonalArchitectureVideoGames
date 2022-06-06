import sqlite3
import functools

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_videogames.domain.videogame import (Videogame, VideogameRepository)
from app_videogames.domain.videogame.value_object import (
    VideogameName,
    Price,
    VideogameDescription
)
from app_videogames.infrastructure.sqlite.user import UserTable
from app_videogames.infrastructure.sqlite import session_com_rol_clo as crc
from .videogame_setup import VideogameTable
from .videogame_create_model import VideogameCreateModel
from .videogame_update_model import VideogameUpdateModel


engine = create_engine('sqlite:///./db/app_videogames.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class SqliteVideogameRepository(VideogameRepository):

    def get_videogames(self) -> Videogame:
        videogames = session.query(VideogameTable).all()
        return videogames

    def get_videogame_by_id(self, id_videogame: int) -> str:
        videogame = session.query(VideogameTable).filter_by(idVideogame=id_videogame).one()
        return videogame

    def insert_videogame(self, id_user: int, data: VideogameCreateModel) -> str:
        connection = sqlite3.connect("./db/app_videogames.db")
        cursor = connection.cursor()
        num_vdg = cursor.execute('SELECT count(*) FROM videogame').fetchone()
        if num_vdg[0] == 0:
            id_videogame = 0
        elif num_vdg[0] != 0:
            id_videogame = cursor.execute (
                'select idVideogame from videogame order by idVideogame desc limit 1'
            ).fetchone()
            id_videogame = functools.reduce(lambda sub, ele: sub * 10 + ele, id_videogame)
        user = session.query(UserTable).filter_by(idUser=id_user).one()
        name = VideogameName(data.name)
        price = Price(data.price)
        description = VideogameDescription(data.description)
        add_videogame = VideogameTable(
            idVideogame = id_videogame+1,
            name = name.value,
            price = price.value,
            description = description.value,
            idUser = user.idUser)
        session.add(add_videogame)
        crc.session_commit_rollback_close(session)
        return "Videogame created"

    def update_videogame(self, id_videogame: int, data: VideogameUpdateModel) -> str:
        videogame = session.query(VideogameTable).filter_by(idVideogame=id_videogame).one()
        name = VideogameName(data.name)
        price = Price(data.price)
        description = VideogameDescription(data.description)
        videogame.name = name.value
        videogame.price = price.value
        videogame.description = description.value
        session.add(videogame)
        crc.session_commit_rollback_close(session)
        return "Videogame updated"

    def delete_videogame(self, id_videogame: int) -> str:
        videogame = session.query(VideogameTable).filter_by(idVideogame=id_videogame).one()
        session.delete(videogame)
        crc.session_commit_rollback_close(session)
        return "Videogame deleted"
