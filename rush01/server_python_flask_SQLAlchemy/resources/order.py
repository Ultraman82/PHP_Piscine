from flask_restful import Resource, reqparse
from models.order import OrderModel


class Order(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('orderlist',
                        type=str,
                        required=False,
                        help="this field cannot be left blak!")

    def get(self, username):
        order = OrderModel.find_by_username(username)
        if order:
            return order.json()
        return {'message': 'order not found'}, 404

    def post(self, username):
        data = Order.parser.parse_args()
        order = OrderModel(username, **data)
        try:
            order.save_to_db()
        except:
            # Internal Server Error
            return {"message": "An error occured inserting the item."}, 500
        return {"message": "Success"}
        # return item.json(), 201

    def delete(self, username):
        order = OrderModel.find_by_username(username)
        if order:
            try:
                order.delete_from_db()
            except:
                return {"message": "An error occured deleting the item."}, 500
        else:
            return{"message": "Cant find the order"}
        return {'message': 'order deleted'}


class OrderList(Resource):
    def get(self):
        return {'orders': list(map(lambda x: x.json(), OrderModel.query.all()))}
