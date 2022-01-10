import os
import hashlib
from ...domain.login_repository import ILoginRepository
from ..repositories.mysql.schemas.users import Users
from ..repositories.mysql.connection_provider import session


class UsersRepository(ILoginRepository):
    session = session

    def get_user_by_email(self, email: str, password: str):
        try:
            password_encrypt = '{0}{1}'.format(os.getenv('PASSWORD_SECRET_KEY'), password).encode('utf-8')
            password_encrypt = hashlib.sha256(password_encrypt).hexdigest()

            return self.session.query(Users).filter_by(
                email=email,
                password=password_encrypt
            ).first()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()
