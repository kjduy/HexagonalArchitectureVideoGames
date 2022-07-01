from ......domain.user import User
from ......infrastructure.sqlite.user import UserTable


class TestUserTable:

    def test_serialize(self):
        user =   User(1, 'Kevin124', 'test@gmail.com', 'Myp@ssword123')
        real_value = UserTable.serialize(user)
        expected_value = {
            'user_id': 1,
            'username': 'Kevin124',
            'email': 'test@gmail.com',
            'password': 'Myp@ssword123'
        }
        assert real_value == expected_value
