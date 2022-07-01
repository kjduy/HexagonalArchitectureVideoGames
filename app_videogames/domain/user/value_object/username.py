import re


class Username:
    value: str
    def __init__(self, _username: str):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{5,10}$'
        regex = re.compile(pattern)
        result = re.search(regex, _username)
        if not result:
            raise UsernameError(UsernameError.message)
        self.value = _username


class UsernameError(Exception):
    message = 'Username should contain at least ' \
    '5 until 10 letters between uppercase - lowercase and numbers'
