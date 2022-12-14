import csv
import os
from ..models.person import Person

class PersonUseCase:
    def __init__(self):
        self.persons = []
        self.gen_person_array()

    def gen_person_array(self):
        with open("./uofg/assets/data/people_data.csv", "r") as f:
            reader = csv.reader(f)
            for person in reader:
                societies = str.split(person[8].replace("[", "").replace("'", "").replace("]", "").replace('"', "").replace("\\", "").replace("{", "").replace("}", ""), ',')
                for i in range(0,len(societies)):
                    societies[i] = societies[i].strip()

                p = Person(
                    person[0],
                    person[1],
                    int(person[2]),
                    person[3],
                    int(person[4]),
                    person[5],
                    int(person[6]),
                    person[7],
                    societies
                )
                
                self.persons.append(p)

    def get_person_by_student_id(self, id):
        for person in self.persons:
            if person.student_id == id:
                return person
        
        return "Not found!"