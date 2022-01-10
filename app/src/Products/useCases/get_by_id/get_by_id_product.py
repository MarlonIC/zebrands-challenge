from ...infrastructure.repositories.product_repository import ProductRepository
from ...infrastructure.repositories.audit_repository import AuditRepository
from ...infrastructure.repositories.mysql.schemas.audit import Audit


class GetByIdProduct:
    def execute(self, product_id: int, ip: str):
        product_repository = ProductRepository()
        product = product_repository.get_by_id(product_id)

        if product is None:
            return product

        audit_repository = AuditRepository()
        audit_dto = Audit(
            ip=ip,
            product_id=product_id
        )
        audit_repository.save(audit_dto)

        return self.dtoRecord(product)

    def dtoRecord(self, schema):
        return {
            'name': schema.name,
            'sku': schema.sku,
            'price': float(round(schema.price, 2)),
            'brand': schema.brand
        }
