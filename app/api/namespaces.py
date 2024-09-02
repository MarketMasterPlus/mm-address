# mm-address/app/api/namespaces.py

from flask_restx import Namespace

# Creating a namespace for address operations
address_ns = Namespace('addresses', description='Operations related to addresses')
