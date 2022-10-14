from dataclasses import dataclass
from location import Location

@dataclass
class Place(frozen=True):
  building_name: str
  opening_times: str
  description: str
  location: Location