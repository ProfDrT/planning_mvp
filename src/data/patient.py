from dataclasses import dataclass

@dataclass
class Patient:
    id: int
    name: str
    age: int
    medical_history: str
    appointment_reason: str