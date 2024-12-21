import unittest
from app import app
from business.cart_factory import CartFactory
from business.cart_services import get_all_cart_item, add_cart_item  # Adjust based on new structure
from database.database import db  # Import db from the correct module

class CartTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the test app and database
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_cart.db'  # File-based test database
        cls.client = app.test_client()

    def setUp(self):
        # Create all tables and start with a clean state before each test
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up database after tests
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_cart_item(self):
        # Test adding a cart item
        with app.app_context():  # Ensure we are within app context here
            cart_item = add_cart_item('Kaws Shirt','https://image.uniqlo.com/UQ/ST3/my/imagesgoods/477815/item/mygoods_69_477815_3x4.jpg?width=369',36, 1)
            self.assertEqual(cart_item.product_name, 'Kaws Shirt')
            self.assertEqual(cart_item.product_price, 36)
            self.assertEqual(cart_item.product_quantity, 1)
            self.assertEqual(cart_item.product_image, 'https://image.uniqlo.com/UQ/ST3/my/imagesgoods/477815/item/mygoods_69_477815_3x4.jpg?width=369')

    def test_get_all_cart_items(self):
        with app.app_context():
            add_cart_item('Kaws Shirt','https://image.uniqlo.com/UQ/ST3/my/imagesgoods/477815/item/mygoods_69_477815_3x4.jpg?width=369',36, 1)
            add_cart_item('Snoopy Shirt', 'https://image.uniqlo.com/UQ/ST3/eu/imagesgoods/471799/item/eugoods_00_471799_3x4.jpg?width=250', 39.9, 2)
            result = get_all_cart_item()
            self.assertEqual(len(result['items']), 2)
            self.assertEqual(result['original_total'], 115.8)
            self.assertEqual(result['discounted_total'], 115.8)

    def test_discounted_total(self):
        with app.app_context():
            original_price = 250
            discounted_price = CartFactory.apply_discount(original_price)
            self.assertEqual(discounted_price, 225)

    def test_calculate_discount(self):
        with app.app_context():
            no_discount_price = 150
            discount_apply_price = 250
            self.assertEqual(CartFactory.calculate_discount(no_discount_price), 0)
            self.assertEqual(CartFactory.calculate_discount(discount_apply_price), 0.10)

    def test_cart_endpoint(self):
        with app.app_context():
            response = self.client.post('/api/cart/', json={
                "product_name": "Kaws Shirt",
                "product_quantity": 1,
                "product_price": 50,
                "product_image" : "https://image.uniqlo.com/UQ/ST3/my/imagesgoods/477815/item/mygoods_69_477815_3x4.jpg?width=369"
            })
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertEqual(data["product_name"], "Kaws Shirt")

            response = self.client.get('/api/cart/')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            print(data)
            self.assertEqual(data["items"][0]['product_name'], "Kaws Shirt")
            self.assertIn("original_total", data)
            self.assertIn("discounted_total", data)

if __name__ == '__main__':
    unittest.main()
