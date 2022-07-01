import pytest

from ......domain.user import User
from ......infrastructure.sqlite.user import SqliteUserRepository, UserCreateModel, UserUpdateModel
from ......infrastructure.sqlite import open_session


class TestSqliteUserRepository:

    @pytest.fixture
    def _mocker_session(self):
        open_session.SqliteRepository.__init__(self)

    @pytest.fixture
    def _user_factory(self):
        user = User(1, 'Kevin123', 'test@test.com', 'Myp@ssword123')
        return user

    def test_get_users(self, _mocker_session, _user_factory):
        users = SqliteUserRepository.get_users(self)
        assert _user_factory.user_id == users[0].user_id
        assert _user_factory.username== users[0].username
        assert _user_factory.email == users[0].email
        assert None is users[0].password

    def test_get_user_by_id(self, _mocker_session, _user_factory):
        user = SqliteUserRepository.get_user_by_id(self, 1)
        assert _user_factory.user_id == user['user_id']
        assert _user_factory.username == user['username']
        assert _user_factory.email == user['email']

    def test_insert_user(self, mocker, _mocker_session, _user_factory):
        user_to_insert = UserCreateModel(
            username=_user_factory.username,
            email=_user_factory.email,
            password=_user_factory.password
        )
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        user = SqliteUserRepository.insert_user(self, user_to_insert)
        assert user == 'User created'

    def test_update_user(self, mocker, _mocker_session, _user_factory):
        user_to_update = UserUpdateModel(
            username=_user_factory.username,
            password=_user_factory.password
        )
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        user = SqliteUserRepository.update_user(self, 1, user_to_update)
        assert user == 'User updated'

    def test_delete_user(self, mocker, _mocker_session):
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        user = SqliteUserRepository.delete_user(self, 1)
        assert user == 'User deleted'

    def test_authenticate_user_when_password_is_incorrect(self, _mocker_session):
        user = SqliteUserRepository.authenticate_user(self, 'test@test.com', 'Checkpassword')
        assert user is False

    def test_authenticate_user_when_password_is_correct(self, _mocker_session, _user_factory):
        user = SqliteUserRepository.authenticate_user(self, 'test@test.com', 'Myp@ssword123')
        assert _user_factory.user_id == user['user_id']
        assert _user_factory.username == user['username']
        assert _user_factory.email == user['email']
