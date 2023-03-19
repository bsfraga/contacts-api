from flask import Blueprint, Flask, jsonify
from flask_restx import Api


# declare resources here
from resources.contacts import Contacts, contacts_ns


app = Flask(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint, doc='/docs/',
            title='My contacts API',
            version='1.0',
            description='A simple contacts API',
            )

app.config['PROPAGATE_EXCEPTIONS'] = True

api.add_namespace(contacts_ns, path='/contacts')

contacts_ns.add_resource(Contacts, '/')

if __name__ == '__main__':
    app.register_blueprint(blueprint)
    app.run(debug=True)
