from flask import Flask
from flask_migrate import Migrate
from .models import db

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cart.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)
