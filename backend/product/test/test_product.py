import unittest
from app import app
from database.database import db
from business.product_services import create_product, get_all_products

class ProductTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_product.db'
        cls.client = app.test_client()

    def setUp(self):
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_products(self):
        with app.app_context():
            product_item = create_product("White T-Shirt", 40, "https://example.com/image1.jpg")
            self.assertEqual(product_item.name, 'White T-Shirt')
            self.assertEqual(product_item.price, 40)
            self.assertEqual(product_item.image_url, "https://example.com/image1.jpg")

    def test_get_products(self):
        with app.app_context():
            create_product("White T-Shirt", 40, "https://example.com/image1.jpg")
            create_product("Black T-Shirt", 30, "https://example.com/image2.jpg")
            result = get_all_products()
            self.assertEqual(len(result), 2)

    def test_product_endpoint(self):
        response = self.client.post('/api/products/', json={
            "name": "White T-Shirt",
            "price": 40,
            "image_url": "https://example.com/image1.jpg"
        })
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(len(data) >= 1)

if __name__ == '__main__':
    unittest.main()
