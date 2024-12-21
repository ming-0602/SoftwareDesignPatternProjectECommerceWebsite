from flask import Flask
from flask_cors import CORS
from database.database import init_app
from routes.product_routes import api_bp

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'  # Path to the database
CORS(app)
init_app(app)  # Initialize the database
app.register_blueprint(api_bp)  # Register routes

@app.route('/')
def hello_world():
    return 'Welcome to the Product Domain!'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
