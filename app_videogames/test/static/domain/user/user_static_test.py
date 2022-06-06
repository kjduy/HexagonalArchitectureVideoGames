from app_videogames.domain.user import User


def test_get_safe_users():
    list_users = [
        User (
            username="Kevin124",
            email="kevin.duy@ioet.com",
            id_user=1,
            password="Changep@ssword124"
        )
    ]
    real_value = User.get_safe_users(list_users)
    expected_value = [
        User (
            username="Kevin124",
            email="kevin.duy@ioet.com",
            id_user=1,
            password="Changep@ssword124"
        )
    ]
    del expected_value[0].password

    assert real_value[0].username == expected_value[0].username
    assert real_value[0].email == expected_value[0].email
    assert real_value[0].id_user == expected_value[0].id_user
