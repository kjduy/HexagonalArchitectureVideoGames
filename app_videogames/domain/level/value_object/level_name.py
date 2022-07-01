import re


class LevelName:
    value: str
    def __init__(self, _level_name: str):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[ ])[A-Za-z ]{1,100}$'
        regex = re.compile(pattern)
        result = re.search(regex, _level_name)
        if not result:
            raise LevelNameError(LevelNameError.message)
        self.value = _level_name


class LevelNameError(Exception):
    message = 'The name can only contain letters or numbers'
        