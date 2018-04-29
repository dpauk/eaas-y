from flask import Blueprint, jsonify

# from project import app
from project.api.models.encryptor import Encryptor


encrypt_blueprint = Blueprint('encrypt', __name__)


@encrypt_blueprint.route('/encrypt/<plaintext>', methods=['GET'])
def encrypt_value(plaintext):
    """Encrypts a value passed to the API call"""
    encryptor = Encryptor()
    ciphertext = encryptor.encrypt(plaintext)
    response_object = {
        'status': 'success',
        'data': {
            'ciphertext': ciphertext,
        }
    }
    return jsonify(response_object), 200



# @encrypt_blueprint.route('/encrypt/ping', methods=['GET'])
# def ping_pong():
#     return jsonify({
#         'status': 'success',
#         'message': 'pong!'
#     })
