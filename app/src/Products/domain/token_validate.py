import os
import jwt
from functools import wraps
from flask import request
from jwt.exceptions import InvalidTokenError
from .response import invalid_access_token, abort_internal_server_error
from .constants import Rol
from ..infrastructure.repositories.mysql.connection_provider import session
from ..infrastructure.repositories.mysql.schemas.users import Users


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = None
        bearer_token = None

        if 'Authorization' in request.headers:
            bearer_token = request.headers.get('Authorization')

        if not bearer_token:
            return invalid_access_token()

        try:
            token = bearer_token.split(' ')[1]
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
            user = session.query(Users).filter(
                Users.user_id == data.get('user_id'),
                Users.email == data.get('email'),
                Users.is_admin == Rol.Admin.value
            ).first()

            if user is None:
                return invalid_access_token()
        except InvalidTokenError as e:
            return invalid_access_token()
        except Exception as e:
            abort_internal_server_error(e)

        return f(user, *args, **kwargs)

    return decorated
