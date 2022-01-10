from flask import Blueprint, request
from ...useCases.create_product.create_product_dto import CreateProductDto
from ...useCases.create_product.create_product import CreateProduct
from ...domain.response import abort_internal_server_error, object_created
from ...domain.token_validate import token_required

blueprint_create_product = Blueprint('create_product', __name__)


@blueprint_create_product.route('', methods=['POST'])
@token_required
def create(user):
    try:
        product_json = request.get_json()
        product_dto = CreateProductDto(
            name=product_json.get('name', ''),
            sku=product_json.get('sku', ''),
            price=product_json.get('price', ''),
            brand=product_json.get('brand', '')
        )
        use_case_create_product = CreateProduct()
        use_case_create_product.execute(product_dto)

        return object_created()
    except Exception as error:
        abort_internal_server_error(error)
