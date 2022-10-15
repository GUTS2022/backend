from flask import Blueprint, jsonify
from .use_cases.person_use_case import PersonUseCase 

from uofg.api.use_cases.reports_use_case import ReportUseCase
from .use_cases.location_use_case import LocationUseCase

api = Blueprint('main', __name__)

@api.route("/locations", methods=['GET'])
def locations():
    location_use_case = LocationUseCase()
    return jsonify(location_use_case.locations)

@api.route("/reports", methods=['GET'])
def reports():
    report_use_case = ReportUseCase()
    return jsonify(report_use_case.reports)
    
@api.route("/people", methods=['GET'])
def people():
    people_object = PersonUseCase()
    return jsonify(people_object.all_persons)
