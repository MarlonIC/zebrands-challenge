from ...infrastructure.repositories.product_repository import ProductRepository


class GetAllProduct:
    def execute(self):
        product_repository = ProductRepository()
        products = product_repository.get_all()
        data = []

        for product in products:
            data.append(self.dtoRecord(product))

        return data

    def dtoRecord(self, schema):
        return {
            'name': schema.name,
            'sku': schema.sku,
            'price': float(round(schema.price, 2)),
            'brand': schema.brand
        }
