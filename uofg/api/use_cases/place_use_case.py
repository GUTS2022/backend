import csv

from typing import List
from ..models.place import Place
from ..models.location import Location
from ..models.opening_hours import OpeningHours 

class PlacesUseCase:
    def __init__(self):
        self.places: List[Place] = []
        self.append_to_places()

    def append_to_places(self):
        with open('./uofg/assets/data/location_data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                lat_lon = row[1].split(' ')
                opening_hours = self.format_time(row[2])
                description = row[3]
                
                location = Location(float(lat_lon[0][1:]), float(lat_lon[1][:-1]))
                place = Place(name, location, opening_hours, description)

                self.places.append(place)

    def format_time(self, time_str):
        time_str = time_str.strip().split("-")
        
        start = time_str[0]
        end = time_str[1]

        opening_hours = OpeningHours(start, end)

        return opening_hours

    def get_place_by_name(self, name):
        for place in self.places:
            if place.name == name:
                return place
        
        return "Not found!"