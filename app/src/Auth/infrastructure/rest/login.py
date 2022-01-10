from flask import Blueprint, request
from ...useCases.login.login import Login
from ...useCases.login.login_dto import LoginDto
from ...domain.response import abort_internal_server_error, successful_request

blueprint_login = Blueprint('login', __name__)


@blueprint_login.route('', methods=['POST'])
def login():
    try:
        auth_json = request.get_json()
        login_dto = LoginDto(
            email=auth_json.get('email', ''),
            password=auth_json.get('password', '')
        )
        use_case_login = Login()
        results = use_case_login.execute(login_dto)

        return successful_request(results)
    except Exception as error:
        abort_internal_server_error(error)
