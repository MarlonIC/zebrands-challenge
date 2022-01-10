class CreateProductDto:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.sku = kwargs.get('sku')
        self.price = kwargs.get('price')
        self.brand = kwargs.get('brand')
