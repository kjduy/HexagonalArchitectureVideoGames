import re


class VideogameDescription:
    value: str
    def __init__(self, _description: str):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[ ])[A-Za-z ]{0,200}$'
        regex = re.compile(pattern)
        result = re.search(regex, _description)
        if not result:
            raise VideogameDescriptionError(VideogameDescriptionError.message)
        self.value = _description


class VideogameDescriptionError(Exception):
    message = 'The description can only contain letters or numbers'
        