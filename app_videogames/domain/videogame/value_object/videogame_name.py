import re

class VideogameName:

    _name: str

    def __init__(self, _name: str):

        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[ ])[A-Za-z ]{0,100}$"
        regex = re.compile(pattern) 
        result = re.search(regex, _name)

        if not result:
            raise VideogameNameError(VideogameNameError.message)
        object.__setattr__(self, "value", _name)

class VideogameNameError(Exception):
    message = "The name can only contain letters or numbers"
        