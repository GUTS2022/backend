from flask import Blueprint, jsonify, request
from .use_cases.person_use_case import PersonUseCase 

from uofg.api.use_cases.reports_use_case import ReportUseCase
from .use_cases.location_use_case import LocationUseCase

api = Blueprint('main', __name__)

@api.route("/locations", methods=['GET'])
def locations():
    location_use_case = LocationUseCase()

    if request.args.get('name'):
        name = request.args.get('name')
        obj = location_use_case.get_location_by_name(name)
        return jsonify(obj)

    return jsonify(location_use_case.locations)

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
