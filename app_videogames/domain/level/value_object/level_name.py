import re

class LevelName:

    _name: str

    def __init__(self, _name: str):

        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[ ])[A-Za-z ]{0,100}$"
        regex = re.compile(pattern) 
        result = re.search(regex, _name)

        if not result:
            raise LevelNameError(LevelNameError.message)
        object.__setattr__(self, "value", _name)

class LevelNameError(Exception):
    message = "The name can only contain letters or numbers"
        