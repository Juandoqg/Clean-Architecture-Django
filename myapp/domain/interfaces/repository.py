from abc import ABC, abstractmethod
from myapp.domain.entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: User):
        pass
