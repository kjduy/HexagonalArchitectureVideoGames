from datetime import datetime

class LastGameDate:

    _last_game_date: str

    def __init__(self, _last_game_date: str):
        try:
            datetime.strptime(_last_game_date, '%Y-%m-%d')
            object.__setattr__(self, "value", _last_game_date)
        except LastGameDateError:
            raise LastGameDateError(LastGameDateError.message)

class LastGameDateError(Exception):
    message = "The date format should be %Y-%m-%d"
        