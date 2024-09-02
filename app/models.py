# mm-address/app/models.py

from . import db  # Import the db instance from __init__.py

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    neighborhood = db.Column(db.String(100), nullable=True)
    complement = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f"<Address {self.street}, {self.city}, {self.state}>"
