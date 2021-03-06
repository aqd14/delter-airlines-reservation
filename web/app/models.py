# models.py

from app import db

class Passenger(db.Model):
    __tablename__ = "passengers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    address = db.Column(db.Text, nullable=False)

    '''
    def __init__(self, name, dob, email, address):
        self.name = name
        self.dob = dob
        self.email = email
        self.address = address
    '''

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Plane(db.Model):
    __tablename__ = "planes"

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(30), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    flight_number = db.Column(db.String(30), unique=True, nullable=False)
    '''
    def __init__(self, model, capacity, flight_number):
        self.model = model
        self.capacity = capacity
        self.flight_number = flight_number
    '''
    def __repr__(self):
        return '<model = {} --- capacity = {} --- flight number = {}>'.format(self.model, self.capacity, self.flight_number)


class Flight(db.Model):
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(200), nullable=False)
    destination = db.Column(db.String(200), nullable=False)
    plane_id = db.Column(db.Integer, db.ForeignKey('planes.id'))
    plane = db.relationship("Plane", backref='flights')
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    locale = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'source': self.source,
            'destination': self.destination,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'local': self.locale
        }
    '''
    def __init__(self, source, destination, departure_time, arrival_time, locale):
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.locale = locale
    '''


class AirFare(db.Model):
    __tablename__ = 'airfares'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric, nullable=False)
    description = db.Column(db.String(100), nullable=True)
    '''
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description
    '''

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    booking_date_time = db.Column(db.DateTime, nullable=False)

    passenger_id = db.Column(db.Integer, db.ForeignKey('passengers.id'))
    passenger = db.relationship('Passenger', backref='transactions')

    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'))
    flight = db.relationship('Flight', backref='transactions')

    airfare_id = db.Column(db.Integer, db.ForeignKey('airfares.id'))
    airfare = db.relationship('AirFare', backref='transactions')
