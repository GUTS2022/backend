from dataclasses import dataclass
from .opening_hours import OpeningHours

@dataclass
class Location():
  name: str
  latitude: float
  longitude: float
  opening_hours: OpeningHours