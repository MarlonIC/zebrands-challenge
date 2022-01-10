from flask import Blueprint, request
from ...useCases.update_product.update_product_dto import UpdateProductDto
from ...useCases.update_product.update_product import UpdateProduct
from ...domain.response import abort_internal_server_error, object_updated
from ...domain.token_validate import token_required

blueprint_update_product = Blueprint('update_product', __name__)


@blueprint_update_product.route('/<int:product_id>', methods=['PUT'])
@token_required
def update(user, product_id):
    try:
        product_json = request.get_json()
        product_dto = UpdateProductDto(
            name=product_json.get('name', ''),
            sku=product_json.get('sku', ''),
            price=product_json.get('price', ''),
            brand=product_json.get('brand', '')
        )

        use_case_update_product = UpdateProduct()
        use_case_update_product.execute(product_id, product_dto)

        return object_updated()
    except Exception as error:
        abort_internal_server_error(error)
