from ...domain.constants import State
from ...domain.product_repository import IProductRepository
from ..repositories.mysql.schemas.product import Product
from ..repositories.mysql.connection_provider import session


class ProductRepository(IProductRepository):
    session = session

    def save(self, schema: Product):
        try:
            self.session.add(schema)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()

    def update(self, product_id: int, schema: Product):
        try:
            self.session.query(Product).filter_by(
                product_id=product_id
            ).update({
                Product.name: schema.name,
                Product.price: schema.price,
                Product.sku: schema.sku,
                Product.brand: schema.brand
            }, synchronize_session=False)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()

    def delete(self, product_id: int):
        try:
            self.session.query(Product).filter_by(
                product_id=product_id
            ).update({
                Product.state: State.DEACTIVATE.value
            }, synchronize_session=False)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()

    def get_all(self):
        try:
            return self.session.query(Product).all()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()

    def get_by_id(self, product_id: int):
        try:
            return self.session.query(Product).filter(
                Product.product_id == product_id,
                Product.state == State.ACTIVE.value
            ).first()
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            self.session.close()
