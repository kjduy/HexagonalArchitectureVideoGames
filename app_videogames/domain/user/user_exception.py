class UserNotFoundError(Exception):
    message = "The user you spcecified does not exist."
    def __str__(self):
        return UserNotFoundError.message

class UsersNotFoundError(Exception):
    message = "No users were found."
    def __str__(self):
        return UsersNotFoundError.message

class EmailAlreadyExistsError(Exception):
    message = "The email you specified already exists."
    def __str__(self):
        return EmailAlreadyExistsError.message
