# business/product_services.py

from database.models import Products, db
from business.product_builder import ProductBuilder

def get_all_products():
    return Products.query.all()

def create_product(name, price, image_url):
    # Use the builder pattern to create the product
    builder = ProductBuilder()
    new_product = (
        builder.set_name(name)
        .set_price(price)
        .set_image_url(image_url)
        .build()
    )

    db.session.add(new_product)
    db.session.commit()

    return new_product
