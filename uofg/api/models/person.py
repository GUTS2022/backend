from dataclasses import dataclass
from typing import List

@dataclass
class Person():
  student_id: str
  name: str
  age: int
  sex: str 
  year: int
  subject: str
  height: int
  hair_colour: str
  societies: List[str]