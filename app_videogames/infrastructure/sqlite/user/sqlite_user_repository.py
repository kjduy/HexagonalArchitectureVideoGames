import sqlite3
import functools

from app_videogames.domain.user import (User, UserRepository)
from app_videogames.domain.user.value_object import (Email, Password, Username)
from app_videogames.infrastructure.sqlite import session_com_rol_clo as crc, open_session
from .user_setup import UserTable
from .user_create_model import UserCreateModel
from .user_update_model import UserUpdateModel


class SqliteUserRepository(UserRepository):

    def get_users(self) -> User:
        session = open_session.create_session()
        users = session.query(UserTable).all()
        return User.get_safe_users(users)

    def get_user_by_id(self, user_id: int) -> str:
        session = open_session.create_session()
        user = session.query(UserTable).filter_by(user_id=user_id).one()
        return User.get_safe_user(user)

    def insert_user(self, data: UserCreateModel) -> str:
        session = open_session.create_session()
        connection = sqlite3.connect("./db/app_videogames.db")
        cursor = connection.cursor()
        num_usr = cursor.execute('SELECT count(*) FROM user').fetchone()
        if num_usr[0] == 0:
            user_id = 0
        elif num_usr[0] != 0:
            user_id = cursor.execute (
                'select user_id from user order by user_id desc limit 1'
            ).fetchone()
            user_id = functools.reduce(lambda sub, ele: sub * 10 + ele, user_id)
        email = Email(data.email)
        password = Password(data.password)
        username = Username(data.username)
        add_user = UserTable(
            user_id = user_id+1,
            username = username.value,
            email = email.value.lower(),
            password = password.value)
        session.add(add_user)
        crc.session_commit_rollback_close(session)
        return "User created"

    def update_user(self, user_id: int, data: UserUpdateModel) -> str:
        session = open_session.create_session()
        user = session.query(UserTable).filter_by(user_id=user_id).one()
        password = Password(data.password)
        username = Username(data.username)
        user.password = password.value
        user.username = username.value
        session.add(user)
        crc.session_commit_rollback_close(session)
        return "User updated"

    def delete_user(self, user_id: int) -> str:
        session = open_session.create_session()
        user = session.query(UserTable).filter_by(user_id=user_id).one()
        session.delete(user)
        crc.session_commit_rollback_close(session)
        return "User deleted"

    def authenticate_user(self, email: str, password: str):
        session = open_session.create_session()
        user = session.query(UserTable).filter_by(email=email).one()
        if user.password != password:
            return False
        return UserTable.serialize(user)
