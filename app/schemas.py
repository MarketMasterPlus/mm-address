# mm-address/app/schemas.py
from flask_marshmallow import Marshmallow
from .models import Address

ma = Marshmallow()

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = True  # Optional: if true, deserialization will create model instances.
