import pytest

from ......domain.videogame import Videogame
from ......infrastructure.sqlite.videogame import (
    SqliteVideogameRepository,
    VideogameCreateModel,
    VideogameUpdateModel
)
from ......infrastructure.sqlite import open_session


class TestSqliteVideogameRepository:

    @pytest.fixture
    def _mocker_session(self):
        open_session.SqliteRepository.__init__(self)

    @pytest.fixture
    def _videogame_factory(self, _mocker_session):
        videogame = Videogame(
            1,
            'Super Smash Bros Ultimate',
            60.0,
            'Is a fighting videogame developed by Bandai Namco Entertainment and published by ' \
            'Nintendo for the Nintendo Switch console',
            1
        )
        return videogame

    def test_get_videogames(self, _mocker_session, _videogame_factory):
        videogames = SqliteVideogameRepository.get_videogames(self)
        assert _videogame_factory.videogame_id == videogames[0].videogame_id
        assert _videogame_factory.name == videogames[0].name
        assert _videogame_factory.price == videogames[0].price
        assert _videogame_factory.description == videogames[0].description
        assert _videogame_factory.user_id == videogames[0].user_id

    def test_get_videogame_by_id(self, _mocker_session, _videogame_factory):
        videogame = SqliteVideogameRepository.get_videogame_by_id(self, 1)
        assert _videogame_factory.videogame_id == videogame.videogame_id
        assert _videogame_factory.name == videogame.name
        assert _videogame_factory.price == videogame.price
        assert _videogame_factory.description == videogame.description
        assert _videogame_factory.user_id == videogame.user_id

    def test_insert_videogame(self, mocker, _mocker_session, _videogame_factory):
        videogame_to_insert = VideogameCreateModel(
            name=_videogame_factory.name,
            price=_videogame_factory.price,
            description=_videogame_factory.description
        )
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        videogame = SqliteVideogameRepository.insert_videogame(self, 1, videogame_to_insert)
        assert videogame == 'Videogame created'

    def test_update_videogame(self, mocker, _mocker_session, _videogame_factory):
        videogame_to_update = VideogameUpdateModel(
            name=_videogame_factory.name,
            price=_videogame_factory.price,
            description=_videogame_factory.description
        )
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        videogame = SqliteVideogameRepository.update_videogame(self, 1, videogame_to_update)
        assert videogame == 'Videogame updated'

    def test_delete_videogame(self, mocker, _mocker_session):
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        videogame = SqliteVideogameRepository.delete_videogame(self, 1)
        assert videogame == 'Videogame deleted'
