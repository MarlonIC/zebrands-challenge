from abc import ABC, abstractmethod


class IProductRepository(ABC):
    @abstractmethod
    def save(self, schema):
        pass

    @abstractmethod
    def update(self, product_id: int, schema):
        pass

    @abstractmethod
    def delete(self, product_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, product_id: int):
        pass
