from dataclasses import dataclass

from .opening_hours import OpeningHours
@dataclass
class Report():
  student_id: str
  name: str
  place_name: str
  present_hours: OpeningHours