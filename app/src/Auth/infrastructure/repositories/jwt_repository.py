import os
import jwt
from ...domain.jwt_repository import IJwtRepository


class JwtRepository(IJwtRepository):
    def encode(self, payload: dict):
        return jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')
