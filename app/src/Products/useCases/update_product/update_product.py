import json
from ...infrastructure.repositories.product_repository import ProductRepository
from ...infrastructure.repositories.users_repository import UsersRepository
from ...infrastructure.repositories.ses_repository import SesRepository
from ...useCases.update_product.update_product_dto import UpdateProductDto
from ...infrastructure.repositories.mysql.schemas.product import Product


class UpdateProduct:
    def execute(self, product_id: int, update_product_dto: UpdateProductDto):
        product_repository = ProductRepository()
        data_antigua = product_repository.get_by_id(product_id)
        data_antigua = self.schema_to_json(data_antigua)
        data_nueva = self.dto_to_string(update_product_dto)

        schema = self.dto_to_schema(update_product_dto)
        product_repository.update(product_id, schema)

        ses_repository = SesRepository()
        users_repository = UsersRepository()
        users_admins = users_repository.get_admins()

        template = '''
        <div>Se ha actualizado el Identificador del producto: {} </div><br>
        <div>Data antigua: {} </div><br>
        <div>Data nueva: {} </div>
        '''.format(product_id, json.dumps(data_antigua), json.dumps(data_nueva))

        for user_admin in users_admins:
            ses_repository.send(user_admin.email, 'Registro actualizado', template)

    def dto_to_schema(self, dto: UpdateProductDto) -> Product:
        return Product(
            name=dto.name,
            sku=dto.sku,
            price=dto.price,
            brand=dto.brand
        )

    def schema_to_json(self, schema):
        return {
            'name': schema.name,
            'sku': schema.sku,
            'price': str(round(schema.price, 2)),
            'brand': schema.brand
        }

    def dto_to_string(self, dto: UpdateProductDto):
        return {
            'name': dto.name,
            'sku': dto.sku,
            'price': str(round(dto.price, 2)),
            'brand': dto.brand
        }
