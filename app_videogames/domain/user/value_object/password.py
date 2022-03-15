from dataclasses import dataclass
import re 


@dataclass(init=False, eq=True, frozen=True)
class Password: 
    _password: str
    def __init__(self, _password: str):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,64}$"
        regex = re.compile(pattern) 
        _password = re.search(regex, _password)
        if not _password:
            raise ValueError("Password should contain at least 8 letters between uppercase - lowercase letters, numbers and symbols")
        object.__setattr__(self, "value", _password)
