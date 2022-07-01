from .value_object import LevelName, Difficulty, LastGameDate


class Level:

    def __init__(
        self,
        level_id: int,
        level_name: LevelName,
        difficulty: Difficulty,
        last_game_date: LastGameDate,
        videogame_id: int
    ):
        self.level_id: int = level_id
        self.level_name: LevelName = level_name
        self.difficulty: Difficulty = difficulty
        self.last_game_date: LastGameDate = last_game_date
        self.videogame_id: int = videogame_id
        