from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), unique=True, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    product_image = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Cart(product_name={self.product_name}, product_price={self.product_price}, product_quantity={self.product_quantity}, product_image={self.product_image})"
