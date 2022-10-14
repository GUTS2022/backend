from crypt import methods
from flask import Blueprint, jsonify
from .use_cases.person_use_case import *

api = Blueprint('main', __name__)

@api.route("/", methods=['GET'])
def index():
    return jsonify("angus is a goofy")

@api.route("/getAllPeople", methods=['GET'])
def getAllPeople():
    peopleObject = PersonUseCase()
    return jsonify(peopleObject.genPersonArray())