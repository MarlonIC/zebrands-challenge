from flask import Blueprint, request
from ...useCases.get_by_id.get_by_id_product import GetByIdProduct
from ...domain.response import abort_internal_server_error, successful_request, resource_not_found

blueprint_get_by_id_product = Blueprint('get_by_id_product', __name__)


@blueprint_get_by_id_product.route('/<int:product_id>', methods=['GET'])
def get_by_id(product_id):
    try:
        ip = request.remote_addr
        use_case_get_by_id_product = GetByIdProduct()
        data = use_case_get_by_id_product.execute(product_id, ip)

        if data is None:
            return resource_not_found()

        return successful_request(data)
    except Exception as error:
        abort_internal_server_error(error)
