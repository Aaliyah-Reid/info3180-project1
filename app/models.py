from . import db


class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    num_rooms = db.Column(db.String(80))
    num_bathrooms = db.Column(db.String(80))
    price = db.Column(db.String(80))
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo_filename = db.Column(db.String(255))

    def __init__(self, title, description, num_rooms, num_bathrooms, price, property_type, location, photo_filename):
        self.title = title
        self.description = description
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo_filename = photo_filename

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
    
    def __repr__(self):
        return '<Property %r>' % (self.title)