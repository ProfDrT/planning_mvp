from dataclasses import dataclass
from typing import List

@dataclass
class Staff:
    id: int
    name: str
    role: str
    specialty: str
    availability: List[str]

    def is_available(self, day: str) -> bool:
        return day in self.availability