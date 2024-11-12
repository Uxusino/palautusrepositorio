from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username: str, password: str, password_confirmation: str):
        if not username or not password:
            raise UserInputError("Username and password are required")
        # Check length
        if len(username) < 3:
            raise UserInputError("Username is too short")
        # Check if username within a-z
        if not all('a' <= char <= 'z' for char in username):
            raise UserInputError("Username must only contain lowercase letters in a-z")
        # Check if user already exists
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already in use")
        # Check if password is long enough
        if len(password) < 8:
            raise UserInputError("Password must be longer than 8 symbols")
        # Check if password contains only letters
        if password.isalpha():
            raise UserInputError("Password must contain at least one numerical or special symbol")
        # Check if password and confirmation match
        if password != password_confirmation:
            raise UserInputError("Password and Password Confirmation don't match!")


user_service = UserService()
