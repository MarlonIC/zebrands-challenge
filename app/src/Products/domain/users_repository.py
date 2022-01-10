from abc import ABC, abstractmethod


class IUsersRepository(ABC):
    @abstractmethod
    def get_admins(self):
        pass
