from crypt import methods
from flask import Blueprint, jsonify

api = Blueprint('main', __name__)

@api.route("/", methods=['GET'])
def index():
    return jsonify("angus is a goofy")