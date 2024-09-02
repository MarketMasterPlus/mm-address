# mm-address/app/api/routes.py

from flask import Blueprint, request
from flask_restx import Api, Resource, fields, Namespace
from ..models import db, Address
import requests

# Create the blueprint and API
blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='MM Address API', version='1.0', description='A Web API for managing addresses and integrating with ViaCEP')

# Namespace without additional path prefix
address_ns = Namespace('', description='Operations related to addresses')
api.add_namespace(address_ns)

# Data model for an address
model = address_ns.model('Address', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an address'),
    'street': fields.String(required=True, description='Street name'),
    'city': fields.String(required=True, description='City name'),
    'state': fields.String(required=True, description='State name'),
    'cep': fields.String(required=True, description='Postal code'),
    'neighborhood': fields.String(description='Neighborhood'),
    'complement': fields.String(description='Complement information')
})

# Resource for listing and creating addresses
@address_ns.route('/mm-address/')
class AddressList(Resource):
    @address_ns.marshal_list_with(model)
    def get(self):
        """List all addresses"""
        addresses = Address.query.all()
        return addresses

    @address_ns.expect(model)
    @address_ns.marshal_with(model, code=201)
    def post(self):
        """Create a new address"""
        data = request.json
        address = Address(**data)
        db.session.add(address)
        db.session.commit()
        return address, 201

# Resource for fetching, updating, and deleting a single address
@address_ns.route('/mm-address/<int:id>')
@address_ns.response(404, 'Address not found')
@address_ns.param('id', 'The address identifier')
class AddressDetail(Resource):
    @address_ns.marshal_with(model)
    def get(self, id):
        """Fetch an address given its identifier"""
        address = Address.query.get_or_404(id)
        return address

    @address_ns.expect(model)
    @address_ns.marshal_with(model)
    def put(self, id):
        """Update an address"""
        address = Address.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(address, key, value)
        db.session.commit()
        return address

    @address_ns.response(204, 'Address deleted')
    def delete(self, id):
        """Delete an address"""
        address = Address.query.get_or_404(id)
        db.session.delete(address)
        db.session.commit()
        return '', 204

# Resource for ViaCEP integration
@address_ns.route('/viacep/<cep>')
@address_ns.param('cep', 'The postal code to lookup')
@address_ns.response(400, 'Invalid postal code format')
class ViaCEP(Resource):
    @address_ns.doc('get_address_by_cep')
    @address_ns.marshal_with(model)
    def get(self, cep):
        """Fetch address information via ViaCEP API"""
        if len(cep) != 8 or not cep.isdigit():
            address_ns.abort(400, 'Invalid postal code format')

        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            data = response.json()
            if 'erro' not in data:
                return {
                    'street': data.get('logradouro'),
                    'city': data.get('localidade'),
                    'state': data.get('uf'),
                    'cep': data.get('cep'),
                    'neighborhood': data.get('bairro'),
                    'complement': data.get('complemento')
                }, 200
            else:
                return {'message': 'CEP not found'}, 404
        else:
            return {'message': 'Failed to retrieve data from ViaCEP'}, response.status_code
