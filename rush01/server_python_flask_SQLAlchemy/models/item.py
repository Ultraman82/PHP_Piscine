from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    imgpath = db.Column(db.String(20))
    manufact = db.Column(db.String(20))
    group = db.Column(db.String(20))
    descript = db.Column(db.String(300))

    def __init__(self, name, price, imgpath, manufact, descript, group):

        self.name = name
        self.price = price
        self.imgpath = imgpath
        self.manufact = manufact
        self.descript = descript
        self.group = group
    #    self.stor_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'imgpath': self.imgpath, "id": self.id,
                'manufact': self.manufact, 'descript': self.descript, 'group': self.group}

    @classmethod
    def find_by_name(cls, name):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(name=name).first()

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
