from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

@dataclass
class Appointment:
    patient_id: int
    doctor_id: int
    nurse_id: int
    room_id: int
    start_time: datetime
    duration: int  # in minutes

@dataclass
class Schedule:
    date: datetime
    appointments: Dict[int, Appointment]

    def add_appointment(self, appointment: Appointment):
        self.appointments[appointment.patient_id] = appointment

    def remove_appointment(self, patient_id: int):
        if patient_id in self.appointments:
            del self.appointments[patient_id]

    def get_appointment(self, patient_id: int) -> Appointment:
        return self.appointments.get(patient_id)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "date": self.date.isoformat(),
            "appointments": {
                patient_id: {
                    "patient_id": appt.patient_id,
                    "doctor_id": appt.doctor_id,
                    "nurse_id": appt.nurse_id,
                    "room_id": appt.room_id,
                    "start_time": appt.start_time.isoformat(),
                    "duration": appt.duration
                } for patient_id, appt in self.appointments.items()
            }
        }