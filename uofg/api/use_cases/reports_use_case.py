import csv

from typing import List
from ..models.report import Report
from ..models.opening_hours import OpeningHours

class ReportUseCase:
    def __init__(self):
        self.reports: List[Report] = []
        self.append_to_reports()

    def append_to_reports(self):
        with open('./uofg/assets/data/security_logs.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                report = Report(row[0], row[1], row[2], self.format_time(row[3]))
                self.reports.append(report)

    def format_time(self, time_str):
        # print(time_str)
        time_str = time_str.strip().split("-")
        
        start = time_str[0]
        end = time_str[1]

        opening_hours = OpeningHours(start, end)

        return opening_hours

    def get_report_by_id(self, id):
        for report in self.reports:
            if report.student_id == id:
                return report
        
        return "Not found!"

    def get_all_reports_for_person(self, id):
        reports = []
        for report in self.reports:
            if report.student_id == id:
                reports.append(report)

        return reports

    def get_reports_at_time(self, time):
        reports = []
        for report in self.reports:
            if report.present_hours.start_time > report.present_hours.end_time:
                report.present_hours.end_time = str(int(report.present_hours.end_time) + 2400)

            if report.present_hours.start_time <= time <= report.present_hours.end_time:
                print(report.present_hours.start_time + "is less than" + time + "d_time:which is less than " + report.present_hours.end_time)
                reports.append(report)

        return reports