from dataclasses import dataclass

from .location import Location
from .opening_hours import OpeningHours

@dataclass
class Place():
  name: str
  location: Location
  opening_hours: OpeningHours
  description: str