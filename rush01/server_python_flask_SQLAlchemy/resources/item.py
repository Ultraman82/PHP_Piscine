from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()    
    parser.add_argument('price',
                        type=float,
                        required=False,
                        help="this field cannot be left blak!")
    parser.add_argument('manufact',
                        type=str,
                        required=False,
                        help="")
    parser.add_argument('descript',
                        type=str,
                        required=True,
                        help="")
    parser.add_argument('imgpath',
                        type=str,
                        required=True,
                        help="")
    parser.add_argument('group',
                        type=str,
                        required=False,
                        help="")

    def put(self, name):
        data = Item.parser.parse_args()        
        item = ItemModel.find_by_name(name)
        print(data)
        if item is None:
            item = ItemModel(name, **data)

        else:
            item.name = data['name']
            item.price = data['price']
            item.imgpath = data['imgpath']
            item.manufact = data['manufact']
            item.descript = data['descript']
            item.group = data['group']

        item.save_to_db()
        return item.json()

    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return({'mesage': 'Item deleted'})

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name `{}` already exists".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()

        except:
            # Internal Server Error
            return {"message": "An error occured inserting the item."}, 500
        return {"message": "Success"}
        # return item.json(), 201

   
class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        # return {'items': [item.json() for item in ItemModel.query.all()]}class ItemList(Resource):

    def delete(self):
        ItemModel.delete_all()
        return({'mesage': 'All Itemlist deleted'})


class ItemEdit(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=False)
    parser.add_argument('price',
                        type=float,
                        required=False)
    parser.add_argument('manufact',
                        type=str,
                        required=False,
                        help="")
    parser.add_argument('descript',
                        type=str,
                        required=False,
                        help="")
    parser.add_argument('imgpath',
                        type=str,
                        required=False,
                        help="")
    parser.add_argument('group',
                        type=str,
                        required=False,
                        help="")

    def put(self, id):
        data = ItemEdit.parser.parse_args()        
        item = ItemModel.find_by_id(id)

        item.name = data['name']
        item.price = data['price']
        item.imgpath = data['imgpath']
        item.manufact = data['manufact']
        item.descript = data['descript']
        item.group = data['group']

        item.save_to_db()
        return item.json()

    def get(self, id):

        item = ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, id):
        if ItemModel.find_by_id(id):
            return {'message': "An item with id `{}` already exists".format(id)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(id, **data)

        try:
            item.save_to_db()

        except:
            # Internal Server Error
            return {"message": "An error occured inserting the item."}, 500
        return {"message": "Success"}
        # return item.json(), 201

    def delete(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            item.delete_from_db()
        return({'mesage': 'Item deleted'})
