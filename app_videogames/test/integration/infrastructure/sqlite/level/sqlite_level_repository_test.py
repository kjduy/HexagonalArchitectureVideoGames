import pytest

from ......domain.level import Level
from ......infrastructure.sqlite.level import (
    SqliteLevelRepository,
    LevelCreateModel,
    LevelUpdateModel
)
from ......infrastructure.sqlite import open_session


class TestSqliteLevelRepository:

    @pytest.fixture
    def _mocker_session(self):
        open_session.SqliteRepository.__init__(self)

    @pytest.fixture
    def _level_factory(self):
        level = Level(1, 'First Level', 'Easy', '2022-04-28', 1)
        return level

    def test_get_levels(self, _mocker_session, _level_factory):
        levels = SqliteLevelRepository.get_levels(self)
        assert _level_factory.level_id == levels[0].level_id
        assert _level_factory.level_name == levels[0].name
        assert _level_factory.difficulty == levels[0].difficulty
        assert _level_factory.last_game_date + ' 00:00:00' == levels[0].last_game_date
        assert _level_factory.videogame_id == levels[0].videogame_id

    def test_get_level_by_id(self, _mocker_session, _level_factory):
        level = SqliteLevelRepository.get_level_by_id(self, 1)
        assert _level_factory.level_id == level.level_id
        assert _level_factory.level_name == level.name
        assert _level_factory.difficulty == level.difficulty
        assert _level_factory.last_game_date + ' 00:00:00' == level.last_game_date
        assert _level_factory.videogame_id == level.videogame_id

    def test_insert_level(self, mocker, _mocker_session, _level_factory):
        level_to_insert = LevelCreateModel(
            name=_level_factory.level_name,
            difficulty=_level_factory.difficulty,
            last_game_date=_level_factory.last_game_date
        )
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        level = SqliteLevelRepository.insert_level(self, 1, level_to_insert)
        assert level == 'Level created'

    def test_update_level(self, mocker, _mocker_session, _level_factory):
        level_to_update = LevelUpdateModel(
            name=_level_factory.level_name,
            difficulty=_level_factory.difficulty,
            last_game_date=_level_factory.last_game_date
        )
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        level = SqliteLevelRepository.update_level(self, 1, level_to_update)
        assert level == 'Level updated'

    def test_delete_level(self, mocker, _mocker_session):
        mocker.patch(
            'app_videogames.infrastructure.sqlite.session_com_rol_clo.session_commit_rollback_close'
        ).return_value=Exception
        level = SqliteLevelRepository.delete_level(self, 1)
        assert level == 'Level deleted'
