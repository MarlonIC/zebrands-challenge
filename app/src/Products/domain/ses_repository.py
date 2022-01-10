from abc import ABC, abstractmethod


class ISesRepository(ABC):
    @abstractmethod
    def send(self, email, subject, body_html):
        pass
