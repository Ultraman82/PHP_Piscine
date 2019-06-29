from db import db


class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    orderlist = db.Column(db.String(300))

    def __init__(self, username, orderlist):

        self.username = username
        self.orderlist = orderlist

    def json(self):
        return {'username': self.username, 'oderlist': self.orderlist}

    @classmethod
    def find_by_username(cls, username):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(id=id).first()

    @classmethod
    def delete_all(cls):
        # SELECT * FROM items WHERE name=name LIMIT 1
        db.session.query(cls).delete()
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def drop_table(self):
        self.drop()
        db.session.commit()
