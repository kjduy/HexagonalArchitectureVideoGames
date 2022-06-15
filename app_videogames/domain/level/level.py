from app_videogames.domain.level.value_object import (LevelName, Difficulty, LastGameDate)


class Level:

    def __init__(
        self,
        id_level: int,
        level_name: LevelName,
        difficulty: Difficulty,
        last_game_date: LastGameDate,
        id_videogame: int
    ):
        self.id_level: int = id_level
        self.level_name: LevelName = level_name
        self.difficulty: Difficulty = difficulty
        self.last_game_date: LastGameDate = last_game_date
        self.id_videogame: int = id_videogame
        