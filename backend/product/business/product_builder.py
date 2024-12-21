# business/product_builder.py

from database.models import Products

class ProductBuilder:
    def __init__(self):
        self._product = Products()

    def set_name(self, name):
        self._product.name = name
        return self

    def set_price(self, price):
        self._product.price = price
        return self

    def set_image_url(self, image_url):
        self._product.image_url = image_url
        return self

    def build(self):
        # Validation or additional logic before returning the object
        if not self._product.name or not self._product.price or not self._product.image_url:
            raise ValueError("All product fields must be set")
        return self._product
