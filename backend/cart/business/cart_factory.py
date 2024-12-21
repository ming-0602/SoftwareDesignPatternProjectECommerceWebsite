from database.models import Cart

class CartFactory:
    @staticmethod
    def create_cart(product_name, product_image, product_price, product_quantity):
        # Create the Cart item with the original price
        cart_item = Cart(
            product_name=product_name,
            product_image=product_image,
            product_price=product_price,
            product_quantity=product_quantity
        )

        # Calculate totals for display purposes
        cart_item.original_total = product_price * product_quantity
        cart_item.discounted_total = CartFactory.apply_discount(cart_item.original_total)

        return cart_item

    @staticmethod
    def apply_discount(total_price):
        # Apply discount based on eligibility
        print(f"this is the apply_discount total_price: {total_price}")
        discount = CartFactory.calculate_discount(total_price)
        return total_price * (1 - discount)

    @staticmethod
    def calculate_discount(total_price):
        # Determine discount rate based on the price threshold
        return 0.10 if total_price >= 200 else 0
