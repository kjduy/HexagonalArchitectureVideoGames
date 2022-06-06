class Email:
    value: str
    def __init__(self, _email: str):
        if not "@" in _email:
            raise EmailError(EmailError.message)
        self.value = _email


class EmailError(Exception):
    message = "Invalid email: it's necesary that email contain a @"
        