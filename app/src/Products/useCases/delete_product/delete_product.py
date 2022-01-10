from ...infrastructure.repositories.product_repository import ProductRepository


class DeleteProduct:
    def execute(self, product_id: int):
        product_repository = ProductRepository()
        product_repository.delete(product_id)
