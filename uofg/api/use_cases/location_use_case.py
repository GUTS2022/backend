import csv

from typing import List
from ..models.location import Location
from ..models.opening_hours import OpeningHours 

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
                opening_hours = self.format_time(row[2])

                location = Location(name, float(lat_lon[0][1:]), float(lat_lon[1][:-1]), opening_hours)
                self.locations.append(location)

    def format_time(self, time_str):
        time_str = time_str.split("-")
        time_str = "".join(time_str)
        time_with_colon = time_str[:4] + ":" + time_str[4:]
        time_with_colon = time_with_colon.split(":")
        
        hours = time_with_colon[0]
        minutes = time_with_colon[1]

        opening_hours = OpeningHours(hours, minutes)

        return opening_hours

    def get_location_by_name(self, name):
        for location in self.locations:
            if location.name == name:
                return location
        
        return "Not found!"