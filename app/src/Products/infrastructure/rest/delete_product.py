from flask import Blueprint
from ...useCases.delete_product.delete_product import DeleteProduct
from ...domain.response import abort_internal_server_error, object_deleted
from ...domain.token_validate import token_required

blueprint_delete_product = Blueprint('delete_product', __name__)


@blueprint_delete_product.route('/<int:product_id>', methods=['DELETE'])
@token_required
def delete(user, product_id):
    try:
        use_case_delete_product = DeleteProduct()
        use_case_delete_product.execute(product_id)

        return object_deleted()
    except Exception as error:
        abort_internal_server_error(error)
