
class UserErrors(Exception):
    def __init__(self, message):
        self.message = message

class UserNotExistsError(UserErrors):
    pass

class IncorrectPasswordError(UserErrors):
    pass

class UserAlreadyRegisteredError(UserErrors):
    pass

class InvalidEmailError(UserErrors):
    pass

