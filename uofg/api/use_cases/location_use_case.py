import csv

from typing import List
from ..models.location import Location

class LocationUseCase:
    def __init__(self):
        self.locations: List[Location] = []
        self.append_to_locations()

    def append_to_locations(self):
        with open('./uofg/assets/data/location_data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                lat_lon = row[1].split(' ')
                location = Location(name, float(lat_lon[0][1:]), float(lat_lon[1][:-1]))
                self.locations.append(location)

    def get_location_by_name(self, name):
        for location in self.locations:
            if location.name == name:
                return location
        
        return "Not found!"