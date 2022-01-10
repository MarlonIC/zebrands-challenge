from flask import Blueprint
from ...useCases.get_all.get_all_product import GetAllProduct
from ...domain.response import abort_internal_server_error, successful_request

blueprint_get_all_product = Blueprint('get_all_product', __name__)


@blueprint_get_all_product.route('', methods=['GET'])
def get_all():
    try:
        use_case_get_all_product = GetAllProduct()
        data = use_case_get_all_product.execute()

        return successful_request(data)
    except Exception as error:
        abort_internal_server_error(error)
