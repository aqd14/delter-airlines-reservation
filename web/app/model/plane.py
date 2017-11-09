from app import db

class Plane(db.Model):
    __tablename__ = "planes"

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    flight_number = db.Column(db.String, nullable=False)

    def __init__(self, model, capacity, flight_number):
        self.model = model
        self.capacity = capacity
        self.flight_number = flight_number

    def __repr__(self):
        return '<model = {0} --- capacity = {1} --- flight number = {2}>'.format(self.model, self.capacity, self.flight_number)