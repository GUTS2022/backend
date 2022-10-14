from dataclasses import dataclass

@dataclass
class Location(frozen=True):
  latitude: float
  longitude: float