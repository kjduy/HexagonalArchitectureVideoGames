import re


class Password: 

    _password: str
    
    def __init__(self, _password: str):

        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,64}$"
        regex = re.compile(pattern) 
        result = re.search(regex, _password)
        
        if not result:
            raise PasswordError(PasswordError.message)
        object.__setattr__(self, "value", _password)

class PasswordError(Exception):
    message = "Password should contain at least 8 until 64 letters between uppercase - lowercase, numbers and symbols"
        