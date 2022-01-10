from abc import ABC, abstractmethod


class IJwtRepository(ABC):
    @abstractmethod
    def encode(self, payload: dict):
        pass
