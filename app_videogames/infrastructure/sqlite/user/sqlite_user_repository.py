import sqlite3
import functools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_videogames.domain.user import (User, UserRepository)
from app_videogames.domain.user.value_object import (Email, Password, Username)
from app_videogames.infrastructure.sqlite import session_com_rol_clo as crc
from .user_setup import UserTable
from .user_create_model import UserCreateModel
from .user_update_model import UserUpdateModel


engine = create_engine('sqlite:///./db/app_videogames.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class SqliteUserRepository(UserRepository):

    def get_users(self) -> User:
        users = session.query(UserTable).all()
        return User.get_safe_users(users)

    def get_user_by_id(self, id_user: int) -> str:
        user = session.query(UserTable).filter_by(idUser=id_user).one()
        return User.get_safe_user(user)

    def insert_user(self, data: UserCreateModel) -> str:
        connection = sqlite3.connect("./db/app_videogames.db")
        cursor = connection.cursor()
        num_usr = cursor.execute('SELECT count(*) FROM user').fetchone()
        if num_usr[0] == 0:
            id_user = 0
        elif num_usr[0] != 0:
            id_user = cursor.execute (
                'select idUser from user order by idUser desc limit 1'
            ).fetchone()
            id_user = functools.reduce(lambda sub, ele: sub * 10 + ele, id_user)
        email = Email(data.email)
        password = Password(data.password)
        username = Username(data.username)
        add_user = UserTable(
            idUser = id_user+1,
            username = username.value,
            email = email.value.lower(),
            password = password.value)
        session.add(add_user)
        crc.session_commit_rollback_close(session)
        return "User created"

    def update_user(self, id_user: int, data: UserUpdateModel) -> str:
        user = session.query(UserTable).filter_by(idUser=id_user).one()
        password = Password(data.password)
        username = Username(data.username)
        user.password = password.value
        user.username = username.value
        session.add(user)
        crc.session_commit_rollback_close(session)
        return "User updated"

    def delete_user(self, id_user: int) -> str:
        user = session.query(UserTable).filter_by(idUser=id_user).one()
        session.delete(user)
        crc.session_commit_rollback_close(session)
        return "User deleted"

    def authenticate_user(self, email: str, password: str):
        user = session.query(UserTable).filter_by(email=email).one()
        if user.password != password:
            return False
        return UserTable.serialize(user)
