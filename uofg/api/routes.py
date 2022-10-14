from flask import Blueprint, jsonify
from .use_cases.location_use_case import LocationUseCase

api = Blueprint('main', __name__)

@api.route("/", methods=['GET'])
def index():
    return jsonify("angus is a goofy")

@api.route("/get_all_locations", methods=['GET'])
def get_all_locations():
    location_use_case = LocationUseCase()
    print(location_use_case.locations)
    return jsonify(location_use_case.locations)