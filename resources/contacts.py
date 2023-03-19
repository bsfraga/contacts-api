import logging

from flask import request
from flask_restx import Resource, Namespace, fields
from models.contacts import ContactModel
from services.contacts import ContactsService

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

contacts_ns = Namespace('contacts', 
                       description='Contact operations')
contacts_doc_ns = Namespace('contacts',
                            description='Contact operations')

contacts_model = contacts_ns.model(
    'Contact', {
        'first_name': fields.String(required=True, description='The contact first name'),
        'last_name': fields.String(required=True, description='The contact last name'),
        'email': fields.String(required=True, description='The contact email'),
        'location': fields.Nested(contacts_ns.model('Location', {
            'city': fields.String(required=True, description='The contact city'),
            'country': fields.String(required=True, description='The contact country')
        })),
        'employer': fields.Nested(contacts_ns.model('Employer', {
            'job_title': fields.String(required=True, description='The contact job title'),
            'company': fields.String(required=True, description='The contact company')
        }))
    }
)


class Contacts(Resource):
    @contacts_ns.doc('list_contacts')
    @contacts_ns.marshal_list_with(contacts_model)
    def get(self):
        return ContactsService.get_all()

    @contacts_ns.doc('create_contact')
    @contacts_ns.expect(contacts_model)
    @contacts_ns.marshal_with(contacts_model, code=201)
    def post(self):
        data = request.json
        return ContactsService.create(data), 201