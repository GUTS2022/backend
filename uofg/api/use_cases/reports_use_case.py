import csv

from typing import List
from ..models.report import Report

class ReportUseCase:
    def __init__(self):
        self.reports: List[Report] = []
        self.append_to_reports()

    def append_to_reports(self):
        with open('./uofg/assets/data/security_logs.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                report = Report(row[0], row[1], row[2], row[3])
                self.reports.append(report)

    def get_report_by_id(self, id):
        for report in self.reports:
            if report.student_id == id:
                return report
        
        return "Not found!"