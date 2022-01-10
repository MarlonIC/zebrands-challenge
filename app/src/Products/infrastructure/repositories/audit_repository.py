from ...domain.audit_repository import IAuditRepository
from ..repositories.mysql.schemas.audit import Audit
from ..repositories.mysql.connection_provider import session


class AuditRepository(IAuditRepository):
    session = session

    def save(self, schema: Audit):
        try:
            self.session.add(schema)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()
