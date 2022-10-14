from flask import Blueprint, jsonify

from uofg.api.use_cases.reports_use_case import ReportUseCase
from .use_cases.location_use_case import LocationUseCase

api = Blueprint('main', __name__)

@api.route("/", methods=['GET'])
def index():
    return jsonify("angus is a goofy")

@api.route("/get_all_locations", methods=['GET'])
def get_all_locations():
    location_use_case = LocationUseCase()
    return jsonify(location_use_case.locations)

@api.route("/get_all_reports", methods=['GET'])
def get_all_reports():
    report_use_case = ReportUseCase()
    return jsonify(report_use_case.reports)