from dataclasses import dataclass
from location import Location

@dataclass
class Report(frozen=True):
  student_id: str
  name: str
  time: str
  location: Location