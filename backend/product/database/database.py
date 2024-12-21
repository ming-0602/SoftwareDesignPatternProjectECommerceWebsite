from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db
# db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
