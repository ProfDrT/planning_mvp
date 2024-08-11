import sqlite3
from contextlib import contextmanager

class Database:
    def __init__(self, db_name=":memory:"):
        self.db_name = db_name

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_name)
        try:
            yield conn
        finally:
            conn.close()

    def initialize_tables(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Create Staff table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS staff (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    role TEXT NOT NULL,
                    specialty TEXT,
                    availability TEXT
                )
            ''')
            
            # Create Patients table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER,
                    medical_history TEXT,
                    appointment_reason TEXT
                )
            ''')
            
            # Create Equipment table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS equipment (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    availability TEXT
                )
            ''')
            
            # Create Schedules table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS schedules (
                    id INTEGER PRIMARY KEY,
                    date TEXT NOT NULL,
                    appointments TEXT
                )
            ''')
            
            conn.commit()

    def insert_staff(self, staff):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO staff (name, role, specialty, availability)
                VALUES (?, ?, ?, ?)
            ''', (staff.name, staff.role, staff.specialty, ','.join(staff.availability)))
            conn.commit()

    def insert_patient(self, patient):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO patients (name, age, medical_history, appointment_reason)
                VALUES (?, ?, ?, ?)
            ''', (patient.name, patient.age, patient.medical_history, patient.appointment_reason))
            conn.commit()

    def insert_equipment(self, equipment):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO equipment (name, type, availability)
                VALUES (?, ?, ?)
            ''', (equipment.name, equipment.type, ','.join(equipment.availability)))
            conn.commit()

    def insert_schedule(self, schedule):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO schedules (date, appointments)
                VALUES (?, ?)
            ''', (schedule.date.isoformat(), str(schedule.to_dict())))
            conn.commit()

    def get_all_staff(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM staff')
            return cursor.fetchall()

    def get_all_patients(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM patients')
            return cursor.fetchall()

    def get_all_equipment(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM equipment')
            return cursor.fetchall()

    def get_schedule(self, date):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM schedules WHERE date = ?', (date.isoformat(),))
            return cursor.fetchone()