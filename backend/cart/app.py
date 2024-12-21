from flask import Flask
from flask_cors import CORS
from database.database import init_app
from routes.cart_routes import api_bp

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

# Initialize the app with database configuration
init_app(app)

# Register the routes blueprint
app.register_blueprint(api_bp)

@app.route('/')
def hello_world():
    return 'Cart Domain'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5002, debug=False)
