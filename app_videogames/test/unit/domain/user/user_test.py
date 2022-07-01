from .....domain.user import User


class TestUser:

    def test_get_safe_user(self):
        user =   User(1, 'Kevin124', 'test@gmail.com', 'Myp@ssword123')
        real_value = User.get_safe_user(user)
        expected_value = {'user_id': 1, 'username': 'Kevin124', 'email': 'test@gmail.com'}
        assert real_value == expected_value


    def test_get_safe_users(self):
        list_users = [User(1, 'Kevin124', 'test@gmail.com', 'Myp@ssword123')]
        real_value = User.get_safe_users(list_users)
        expected_value = [User(1, 'Kevin124', 'test@gmail.com', 'Myp@ssword123')]
        del expected_value[0].password
        assert real_value[0].username == expected_value[0].username
        assert real_value[0].email == expected_value[0].email
        assert real_value[0].user_id == expected_value[0].user_id
