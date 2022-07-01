import pytest

from .....domain.level.value_object import (
    Difficulty,
    DifficultyError,
    LastGameDate,
    LevelName,
    LevelNameError
)


class TestLevelValueObject:

    def test_invalid_difficulty(self):
        with pytest.raises(DifficultyError):
            Difficulty('God')


    def test_invalid_last_game_date(self):
        with pytest.raises(ValueError):
            LastGameDate('1 Junio 2022')


    def test_invalid_level_name(self):
        with pytest.raises(LevelNameError):
            LevelName('')
