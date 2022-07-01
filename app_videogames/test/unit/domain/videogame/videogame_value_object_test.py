import pytest

from .....domain.videogame.value_object import (
    Price,
    PriceError,
    VideogameDescription,
    VideogameDescriptionError,
    VideogameName,
    VideogameNameError
)


class TestVideogameValueObject:

    def test_invalid_price(self):
        with pytest.raises(PriceError):
            Price('60.00')


    def test_invalid_videogame_description(self):
        with pytest.raises(VideogameDescriptionError):
            VideogameDescription('123')


    def test_invalid_videogame_name(self):
        with pytest.raises(VideogameNameError):
            VideogameName('123')
