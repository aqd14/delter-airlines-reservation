from app import db

class Passenger(db.Model):
    __tablename__ = "passengers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<name {}>'.format(self.name)