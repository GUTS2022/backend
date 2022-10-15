from crypt import methods
from flask import Blueprint, jsonify
from .use_cases.person_use_case import PersonUseCase 

api = Blueprint('main', __name__)

@api.route("/", methods=['GET'])
def index():
    return jsonify("angus is a goofy")

@api.route("/get_all_people", methods=['GET'])
def get_all_people():
    people_object = PersonUseCase()
    return jsonify(people_object.all_persons)