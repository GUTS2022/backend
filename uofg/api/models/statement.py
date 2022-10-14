from dataclasses import dataclass

@dataclass
class Statement(frozen=True):
  student_id: str
  name: str
  testimony: str