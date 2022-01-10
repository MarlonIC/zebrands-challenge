from ...domain.constants import Rol
from ...domain.users_repository import IUsersRepository
from ..repositories.mysql.schemas.users import Users
from ..repositories.mysql.connection_provider import session


class UsersRepository(IUsersRepository):
    session = session

    def get_admins(self):
        try:
            return self.session.query(Users).filter(
                Users.is_admin == Rol.Admin.value
            ).all()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()
