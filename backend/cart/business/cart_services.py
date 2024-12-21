from database.models import db, Cart
from business.cart_factory import CartFactory

def get_all_cart_item():
    # Retrieve all items in the cart
    cart_items = Cart.query.all()

    # Calculate total original price (sum of individual items' price * quantity)
    total_original = sum(item.product_price * item.product_quantity for item in cart_items)

    # Calculate total discounted price (apply discount to total)
    total_discounted = CartFactory.apply_discount(total_original)

    return {
        "items": cart_items,
        "original_total": total_original,
        "discounted_total": total_discounted
    }

def add_cart_item(product_name, product_image, product_price, product_quantity):
    existing_item = Cart.query.filter_by(product_name=product_name).first()

    if existing_item:
        # If it exists, update the quantity
        existing_item.product_quantity = int(existing_item.product_quantity) + int(product_quantity)
        db.session.commit()
        return existing_item
    else:
        # If it doesn't exist, use the factory to create a new cart item
        new_item = CartFactory.create_cart(product_name, product_image, product_price, product_quantity)
        db.session.add(new_item)  # Add the item to the session
        db.session.commit()       # Commit the changes to the database
        return new_item
