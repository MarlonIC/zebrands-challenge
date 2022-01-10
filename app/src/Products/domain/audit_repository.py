from abc import ABC, abstractmethod


class IAuditRepository(ABC):
    @abstractmethod
    def save(self, schema):
        pass
