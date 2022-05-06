class Price:

    _price: float

    def __init__(self, _price: float):
        if (type(_price) != float):
            raise PriceError(PriceError.message)
        object.__setattr__(self, "value", _price)

class PriceError(Exception):
    message = "Invalid price: must be a decimal"
        