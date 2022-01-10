from ...infrastructure.repositories.product_repository import ProductRepository
from ...useCases.create_product.create_product_dto import CreateProductDto
from ...infrastructure.repositories.mysql.schemas.product import Product


class CreateProduct:
    def execute(self, create_product_dto: CreateProductDto):
        product_repository = ProductRepository()
        schema = self.dto_to_schema(create_product_dto)
        product_repository.save(schema)

    def dto_to_schema(self, dto):
        return Product(
            name=dto.name,
            sku=dto.sku,
            price=dto.price,
            brand=dto.brand
        )
