from myapp.domain.entities.user import User
from myapp.domain.interfaces.repository import IUserRepository

class CreateUser:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, name, email):
        user = User(name=name, email=email)
        self.user_repository.save(user)
