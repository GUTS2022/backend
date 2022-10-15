from flask import Blueprint, jsonify, request

from uofg.api.models.report import Report
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

@api.route("/people/place/<time>", methods=['GET'])
def get_people_place(time):
    place_use_case = PlacesUseCase()
    reports_use_case = ReportUseCase()

    reports_at_time = reports_use_case.get_reports_at_time(time)
    people_at_place_at_time = []

    for report in reports_at_time:
        for place in place_use_case.places:
            if place.name == report.place_name:
                latlong = place.location
        people_at_place_at_time.append({
            "StudentID": report.student_id,
            "StudentName": report.name,
            "PlaceName": report.place_name,
            "Location": latlong,
        })
    
    return jsonify(people_at_place_at_time)
    
@api.route("/people/group/course", methods=['GET'])
def group_by_course():
    person_use_case = PersonUseCase()

    students_in_course = {}
    for person in person_use_case.persons:
        if person.subject in students_in_course:
            students_in_course[person.subject].append(person)
        else:
            students_in_course.update({person.subject:[person]})

    return jsonify(students_in_course)