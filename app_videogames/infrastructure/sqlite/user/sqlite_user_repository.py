import sqlite3
import functools

from ....domain.user import User, UserRepository
from ....domain.user.value_object import Email, Password, Username
from .. import session_com_rol_clo as crc, open_session
from .user_setup import UserTable
from .user_create_model import UserCreateModel
from .user_update_model import UserUpdateModel


class SqliteUserRepository(UserRepository, open_session.SqliteRepository):

    def get_users(self) -> User:
        users = self.session.query(UserTable).all()
        open_session.SqliteRepository.close_session(self.session)
        return User.get_safe_users(users)

    def get_user_by_id(self, user_id: int) -> str:
        user = self.session.query(UserTable).filter_by(user_id=user_id).one()
        open_session.SqliteRepository.close_session(self.session)
        return User.get_safe_user(user)

    def insert_user(self, data: UserCreateModel) -> str:
        connection = sqlite3.connect('./db/app_videogames.db')
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
        self.session.add(add_user)
        crc.session_commit_rollback_close(self.session)
        return 'User created'

    def update_user(self, user_id: int, data: UserUpdateModel) -> str:
        user = self.session.query(UserTable).filter_by(user_id=user_id).one()
        password = Password(data.password)
        username = Username(data.username)
        user.password = password.value
        user.username = username.value
        self.session.add(user)
        crc.session_commit_rollback_close(self.session)
        return 'User updated'

    def delete_user(self, user_id: int) -> str:
        user = self.session.query(UserTable).filter_by(user_id=user_id).one()
        self.session.delete(user)
        crc.session_commit_rollback_close(self.session)
        return 'User deleted'

    def authenticate_user(self, email: str, password: str):
        user = self.session.query(UserTable).filter_by(email=email).one()
        if user.password != password:
            open_session.SqliteRepository.close_session(self.session)
            return False
        open_session.SqliteRepository.close_session(self.session)
        return UserTable.serialize(user)
