from flask import Blueprint, jsonify

api = Blueprint('main', __name__)

@api.route("/")
def index():
    return jsonify("angus is a goofy")