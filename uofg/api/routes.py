from flask import Blueprint, jsonify, request
from .use_cases.person_use_case import PersonUseCase 

from uofg.api.use_cases.reports_use_case import ReportUseCase
from .use_cases.place_use_case import PlacesUseCase

api = Blueprint('main', __name__)

@api.route("/places", methods=['GET'])
def places():
    places_use_case = PlacesUseCase()

    if request.args.get('name'):
        name = request.args.get('name')
        obj = places_use_case.get_place_by_name(name)
        return jsonify(obj)

    return jsonify(places_use_case.places)

@api.route("/reports", methods=['GET'])
def reports():
    report_use_case = ReportUseCase()

    if request.args.get('id'):
        student_id = request.args.get('id')
        obj = report_use_case.get_report_by_id(student_id)
        return jsonify(obj)

    return jsonify(report_use_case.reports)
    
@api.route("/people", methods=['GET'])
def people():
    people_use_case = PersonUseCase()

    if request.args.get('id'):
        student_id = request.args.get('id')
        obj = people_use_case.get_person_by_student_id(student_id)
        return jsonify(obj)

    return jsonify(people_use_case.persons)

@api.route("/get_people_location", methods=['GET'])
def get_people_location(time):
    people_use_case = PersonUseCase()
    location_use_case = LocationUseCase()
    
    