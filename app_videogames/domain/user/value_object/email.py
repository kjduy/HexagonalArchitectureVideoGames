from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class Email:
    _email: str
    def __init__(self, _email: str):
        if not "@" in _email:
            raise ValueError("Invalid email")
        object.__setattr__(self, "value", _email)
        