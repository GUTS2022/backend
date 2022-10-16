from flask import Blueprint, jsonify, request

from uofg.api.models.report import Report
from uofg.api.use_cases.statements_use_case import StatementsUseCase
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
    else:
        return jsonify(people_use_case.persons)

@api.route("/people/travel_log/<student_id>", methods=['GET'])
def travel_log(student_id):
    reports_use_case = ReportUseCase()
    return jsonify(reports_use_case.get_all_reports_for_person(student_id))

@api.route("/people/statement/<student_id>", methods=['GET'])
def get_statement(student_id):
    statement_use_case = StatementsUseCase()
    return jsonify(statement_use_case.get_statement_by_id(student_id))

@api.route("/people/place/<time>", methods=['GET'])
def get_people_place(time):
    place_use_case = PlacesUseCase()
    reports_use_case = ReportUseCase()
    
    if request.args.get('end'):
        reports_at_time = reports_use_case.get_reports_at_time(time, request.args.get('end'))
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

    else:
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

@api.route("/courses", methods=['GET'])
def get_all_courses():
    person_use_case = PersonUseCase()

    courses = []
    for person in person_use_case.persons:
        if person.subject not in courses:
            courses.append(person.subject)

    return jsonify(courses)

@api.route("/societies", methods=['GET'])
def get_all_societies():
    person_use_case = PersonUseCase()

    societies = []
    for person in person_use_case.persons:
        for society in person.societies:
            if society not in societies:
                societies.append(society)

    return jsonify(societies)

@api.route("/statements", methods=['GET'])
def get_all_statements():
    statement_use_case = StatementsUseCase()
    return jsonify(statement_use_case.statements)