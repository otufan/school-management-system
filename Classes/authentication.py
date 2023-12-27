from user import User 

class Authentication:
    _current_user = None

    @classmethod
    def login(cls, user):
        # Set the current user after successful login
        cls._current_user = user

    @classmethod
    def logout(cls):
        # Clear the current user on logout
        cls._current_user = None

    @classmethod
    def get_current_user(cls):
        # Retrieve the current user
        return cls._current_user