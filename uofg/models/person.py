from dataclasses import dataclass
from typing import List

@dataclass
class Person(frozen=True):
  student_id: str
  name: str
  age: int
  sex: bool
  year: int
  subject: str
  height: int
  hair_colour: str
  societes: List[str]