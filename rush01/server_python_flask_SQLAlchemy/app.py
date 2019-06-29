from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, UserList, SaveCart, UserCart
from resources.item import Item, ItemList, ItemEdit
from resources.order import Order, OrderList
#from resources.store import Store, StoreList
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'abcd'

CORS(app)
#CORS(app, resources={r"/api/*": {"Access-Control-Allow-Origin": "127.0.0.1:3000"}})
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Order, '/order/<string:username>')
api.add_resource(OrderList, '/orders')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemEdit, '/itemedit/<int:id>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')
api.add_resource(UserCart, '/user/<string:username>')
api.add_resource(SaveCart, '/cart/<string:username>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
