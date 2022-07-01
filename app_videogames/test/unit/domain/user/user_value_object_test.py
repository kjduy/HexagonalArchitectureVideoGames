import pytest

from .....domain.user.value_object import (
    Email,
    EmailError,
    Password,
    PasswordError,
    Username,
    UsernameError
)


class TestUserValueObject:

    def test_invalid_email(self):
        with pytest.raises(EmailError):
            Email('testgmail.com')


    def test_invalid_password(self):
        with pytest.raises(PasswordError):
            Password('152')


    def test_invalid_username(self):
        with pytest.raises(UsernameError):
            Username('152')
