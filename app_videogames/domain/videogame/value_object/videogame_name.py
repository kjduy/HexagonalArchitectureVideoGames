import re


class VideogameName:
    value: str
    def __init__(self, _videogame_name: str):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[ ])[A-Za-z ]{0,100}$'
        regex = re.compile(pattern)
        result = re.search(regex, _videogame_name)
        if not result:
            raise VideogameNameError(VideogameNameError.message)
        self.value = _videogame_name


class VideogameNameError(Exception):
    message = "The name can only contain letters or numbers"
        