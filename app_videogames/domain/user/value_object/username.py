from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class Username:
    _username: str
    def __init__(self, _username: str):
        if len(_username) < 5:
            raise ValueError("Length should be at least 5")
        elif len(_username) > 10:
            raise ValueError("Length should not be greater than 10")
        if not _username.isalnum():
            raise ValueError("Username only can contain letters and numbers")
        object.__setattr__(self, "value", _username)
        