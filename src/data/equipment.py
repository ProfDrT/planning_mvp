from dataclasses import dataclass
from typing import List

@dataclass
class Equipment:
    id: int
    name: str
    type: str
    availability: List[str]

    def is_available(self, day: str) -> bool:
        return day in self.availability