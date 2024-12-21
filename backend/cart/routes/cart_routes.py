from flask import Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from business.cart_services import get_all_cart_item, add_cart_item

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Define fields for individual cart items
cart_fields = {
    'product_name': fields.String,
    'product_image': fields.String,
    'product_quantity': fields.Integer,
    'product_price': fields.Float,
}

# Define fields for total price information in the response
totals_fields = {
    'items': fields.List(fields.Nested(cart_fields)),
    'original_total': fields.Float,
    'discounted_total': fields.Float,
}

cart_args = reqparse.RequestParser()
cart_args.add_argument('product_name', type=str, required=True, help="This field cannot be blank")
cart_args.add_argument('product_image', type=str, required=True, help="This field cannot be blank")
cart_args.add_argument('product_quantity', type=int, required=True, help="This field cannot be blank")
cart_args.add_argument('product_price', type=float, required=True, help="This field cannot be blank")

class CartResource(Resource):
    @marshal_with(totals_fields)
    def get(self):
        return get_all_cart_item()

    @marshal_with(cart_fields)
    def post(self):
        args = cart_args.parse_args()
        cart_item = add_cart_item(args['product_name'], args['product_image'], args['product_price'], args['product_quantity'])
        return cart_item

api.add_resource(CartResource, '/api/cart/')
