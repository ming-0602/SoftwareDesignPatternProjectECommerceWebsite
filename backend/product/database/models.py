# from database import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Products(name='{self.name}', price={self.price}, image_url={self.image_url})"
