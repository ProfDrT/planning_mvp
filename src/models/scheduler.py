from datetime import datetime, timedelta

class Scheduler:
    def __init__(self, resource_allocator):
        self.resource_allocator = resource_allocator
        self.schedule = {}

    def generate_schedule(self, date):
        # Generate a daily schedule
        self.schedule = {}
        allocation = self.resource_allocator.allocate_resources()

        start_time = datetime.combine(date, datetime.min.time()) + timedelta(hours=9)  # 9 AM start
        end_time = start_time + timedelta(hours=8)  # 8-hour workday

        current_time = start_time
        for patient, resources in allocation.items():
            if current_time >= end_time:
                break  # End of workday

            appointment_duration = timedelta(minutes=30)  # Assume 30-minute appointments
            self.schedule[patient] = {
                'time': current_time,
                'doctor': resources['doctor'],
                'nurse': resources['nurse'],
                'room': resources['room'],
            }
            current_time += appointment_duration

        return self.schedule

    def get_available_slots(self, date):
        # Return available time slots for a given date
        # This is a placeholder implementation
        slots = []
        start_time = datetime.combine(date, datetime.min.time()) + timedelta(hours=9)
        end_time = start_time + timedelta(hours=8)
        current_time = start_time

        while current_time < end_time:
            if current_time not in [appt['time'] for appt in self.schedule.values()]:
                slots.append(current_time)
            current_time += timedelta(minutes=30)

        return slots

    def reschedule_appointment(self, patient, new_time):
        # Reschedule an appointment for a patient
        if patient in self.schedule:
            old_time = self.schedule[patient]['time']
            self.schedule[patient]['time'] = new_time
            return True
        return False