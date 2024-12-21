from flask import Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from business.product_services import get_all_products, create_product

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Argument parsing
product_args = reqparse.RequestParser()
product_args.add_argument("name", type=str, required=True, help="Product name cannot be blank")
product_args.add_argument("price", type=float, required=True, help="Price cannot be blank")
product_args.add_argument("image_url", type=str, required=True, help="Image URL cannot be blank")

# API response fields
product_field = {
    'id': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'image_url': fields.String
}

class ProductResource(Resource):
    @marshal_with(product_field)
    def get(self):
        return get_all_products()

    @marshal_with(product_field)
    def post(self):
        args = product_args.parse_args()
        product = create_product(args['name'], args['price'], args['image_url'])
        return product, 201  # Created successfully

api.add_resource(ProductResource, '/api/products/')
