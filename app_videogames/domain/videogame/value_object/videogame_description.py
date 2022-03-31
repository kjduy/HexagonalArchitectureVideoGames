import re


class VideogameDescription:

    _description: str

    def __init__(self, _description: str):

        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[ ])[A-Za-z ]{0,200}$"
        regex = re.compile(pattern) 
        result = re.search(regex, _description)

        if not result:
            raise VideogameDescriptionError(VideogameDescriptionError.message)
        object.__setattr__(self, "value", _description)

class VideogameDescriptionError(Exception):
    message = "The description can only contain letters or numbers"
        