import re

class Difficulty:

    _difficulty: str

    def __init__(self, _difficulty: str):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])[A-Za-z]{4,6}$"
        regex = re.compile(pattern) 
        result = re.search(regex, _difficulty)

        if not result:
            raise DifficultyError(DifficultyError.message)
        object.__setattr__(self, "value", _difficulty)

class DifficultyError(Exception):
    message = "The difficulty can only be: Easy, Medium or Hard"
        