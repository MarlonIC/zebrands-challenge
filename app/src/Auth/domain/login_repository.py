from abc import ABC, abstractmethod


class ILoginRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str, password: str):
        pass
