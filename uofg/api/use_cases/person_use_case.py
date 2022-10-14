import csv
import os
from ..models.person import Person

class PersonUseCase:
    def __init__(self):
        ...
    def genPersonArray(self):
        persons = []
        with open("./uofg/assets/data/people_data.csv", "r") as f:
            reader = csv.reader(f)
            for person in reader:
                print(person)
                p = Person(
                    person[0],
                    person[1],
                    person[2],
                    person[3],
                    person[4],
                    person[5],
                    person[6],
                    person[7],
                    str.split(person[8], ',') # get rid of spaces and "'"
                )
                persons.append(p)
        
        return persons