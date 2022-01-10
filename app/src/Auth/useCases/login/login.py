from ...infrastructure.repositories.users_repository import UsersRepository
from ...infrastructure.repositories.jwt_repository import JwtRepository
from ...useCases.login.login_dto import LoginDto


class Login:
    def execute(self, login_dto: LoginDto):
        users_repository = UsersRepository()
        jwt_repository = JwtRepository()
        user = users_repository.get_user_by_email(login_dto.email, login_dto.password)
        payload = {
            'user_id': user.user_id,
            'email': user.email,
            'is_admin': user.is_admin
        }

        return {
            'token': jwt_repository.encode(payload)
        }
