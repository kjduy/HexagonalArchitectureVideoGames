class Price:
    value: str
    def __init__(self, _price: float):
        if isinstance(_price) != float:
            raise PriceError(PriceError.message)
        self.value = _price


class PriceError(Exception):
    message = "Invalid price: must be a decimal"
        