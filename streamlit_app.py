import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from src.data.staff import Staff
from src.data.patient import Patient
from src.data.equipment import Equipment
from src.data.schedule import Schedule, Appointment
from src.models.resource_allocator import ResourceAllocator
from src.models.scheduler import Scheduler
from src.utils.database import Database

# Initialize database
db = Database(":memory:")
db.initialize_tables()

def main():
    st.title("OPDPS Planning MVP")
    st.write("Welcome to the Outpatient Department Planning System")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Data Input", "Generate Schedule", "View Resources"])

    if page == "Home":
        home_page()
    elif page == "Data Input":
        data_input_page()
    elif page == "Generate Schedule":
        generate_schedule_page()
    elif page == "View Resources":
        view_resources_page()

def home_page():
    st.write("## Outpatient Department Planning System")
    st.write("This system helps in resource allocation and scheduling for outpatient departments.")
    st.write("Use the sidebar to navigate between different functionalities:")
    st.write("- **Data Input**: Add staff, patients, and equipment data")
    st.write("- **Generate Schedule**: Create a daily schedule based on available resources and patients")
    st.write("- **View Resources**: See an overview of current resources and schedules")

def data_input_page():
    st.write("## Data Input")
    
    input_type = st.selectbox("Select input type", ["Staff", "Patient", "Equipment"])
    
    if input_type == "Staff":
        name = st.text_input("Name")
        role = st.selectbox("Role", ["Doctor", "Nurse", "Technician"])
        specialty = st.text_input("Specialty")
        availability = st.multiselect("Availability", ["Mon", "Tue", "Wed", "Thu", "Fri"])
        
        if st.button("Add Staff"):
            staff = Staff(id=None, name=name, role=role, specialty=specialty, availability=availability)
            db.insert_staff(staff)
            st.success("Staff added successfully!")

    elif input_type == "Patient":
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        medical_history = st.text_area("Medical History")
        appointment_reason = st.text_input("Appointment Reason")
        
        if st.button("Add Patient"):
            patient = Patient(id=None, name=name, age=age, medical_history=medical_history, appointment_reason=appointment_reason)
            db.insert_patient(patient)
            st.success("Patient added successfully!")

    elif input_type == "Equipment":
        name = st.text_input("Name")
        equipment_type = st.text_input("Type")
        availability = st.multiselect("Availability", ["Mon", "Tue", "Wed", "Thu", "Fri"])
        
        if st.button("Add Equipment"):
            equipment = Equipment(id=None, name=name, type=equipment_type, availability=availability)
            db.insert_equipment(equipment)
            st.success("Equipment added successfully!")

def generate_schedule_page():
    st.write("## Generate Schedule")
    
    date = st.date_input("Select Date")
    
    if st.button("Generate Schedule"):
        # Fetch data from database
        staff_data = db.get_all_staff()
        patient_data = db.get_all_patients()
        equipment_data = db.get_all_equipment()
        
        # Convert database data to objects
        staff = [Staff(*s) for s in staff_data]
        patients = [Patient(*p) for p in patient_data]
        equipment = [Equipment(*e) for e in equipment_data]
        
        # Generate schedule
        resource_allocator = ResourceAllocator(staff, patients, equipment)
        scheduler = Scheduler(resource_allocator)
        schedule = scheduler.generate_schedule(date)
        
        # Display schedule
        st.write("### Generated Schedule")
        for patient, appointment in schedule.items():
            st.write(f"Patient: {patient.name}")
            st.write(f"Time: {appointment['time']}")
            st.write(f"Doctor: {appointment['doctor'].name}")
            st.write(f"Nurse: {appointment['nurse'].name}")
            st.write(f"Room: {appointment['room'].name}")
            st.write("---")
        
        # Save schedule to database
        db_schedule = Schedule(date=date, appointments={})
        for patient, appointment in schedule.items():
            db_schedule.add_appointment(Appointment(
                patient_id=patient.id,
                doctor_id=appointment['doctor'].id,
                nurse_id=appointment['nurse'].id,
                room_id=appointment['room'].id,
                start_time=appointment['time'],
                duration=30
            ))
        db.insert_schedule(db_schedule)

def view_resources_page():
    st.write("## View Resources")
    
    resource_type = st.selectbox("Select resource type", ["Staff", "Patients", "Equipment", "Schedules"])
    
    if resource_type == "Staff":
        staff_data = db.get_all_staff()
        df = pd.DataFrame(staff_data, columns=["ID", "Name", "Role", "Specialty", "Availability"])
        st.dataframe(df)
    
    elif resource_type == "Patients":
        patient_data = db.get_all_patients()
        df = pd.DataFrame(patient_data, columns=["ID", "Name", "Age", "Medical History", "Appointment Reason"])
        st.dataframe(df)
    
    elif resource_type == "Equipment":
        equipment_data = db.get_all_equipment()
        df = pd.DataFrame(equipment_data, columns=["ID", "Name", "Type", "Availability"])
        st.dataframe(df)
    
    elif resource_type == "Schedules":
        date = st.date_input("Select Date")
        schedule = db.get_schedule(date)
        if schedule:
            st.write(f"Schedule for {date}")
            st.write(schedule)
        else:
            st.write("No schedule found for the selected date.")

if __name__ == "__main__":
    main()