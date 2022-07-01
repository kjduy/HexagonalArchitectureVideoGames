from datetime import datetime


class LastGameDate:
    value: str
    def __init__(self, _last_game_date: str):
        try:
            _last_game_date = datetime.strptime(_last_game_date, '%Y-%m-%d')
            self.value = _last_game_date
        except LastGameDateError as error:
            raise LastGameDateError(LastGameDateError.message) from error


class LastGameDateError(Exception):
    message = 'The date format should be %Y-%m-%d'
        