# OPDPS Planning MVP

This is the Minimum Viable Product (MVP) for the Outpatient Department Planning System (OPDPS). The system aims to optimize resource allocation and scheduling in outpatient departments.

## Project Structure

```
planning_mvp/
├── streamlit_app.py
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── resource_allocator.py
│   │   ├── scheduler.py
│   │   ├── workload_distributor.py
│   │   └── rl_model.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── staff.py
│   │   ├── patient.py
│   │   ├── equipment.py
│   │   └── schedule.py
│   └── utils/
│       ├── __init__.py
│       └── database.py
├── tests/
│   ├── __init__.py
│   ├── test_resource_allocation.py
│   └── test_schedule_generation.py
├── data/
│   └── sample_hospital_data.csv
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml
```

## Features

- Add and manage staff, patients, and equipment data
- Generate daily schedules based on available resources and patients
- View current resource allocation and schedules

## Setup and Running

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/ProfDrT/opdps_planning.git
   ```
2. Navigate to the project directory:
   ```
   cd opdps_planning_mvp
   ```
3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
6. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

### Streamlit Cloud Deployment

1. Connect your GitHub account to Streamlit Cloud
2. Create a new app in Streamlit Cloud
3. Point it to your GitHub repo: https://github.com/ProfDrT/opdps_planning_mvp
4. Set the main file path to: streamlit_app.py

## Usage

1. Open the app in your web browser (locally or on Streamlit Cloud).
2. Use the sidebar to navigate between different pages:
   - Home: View app description and instructions
   - Data Input: Add staff, patients, and equipment data
   - Generate Schedule: Create a daily schedule based on available resources and patients
   - View Resources: See an overview of current resources and schedules
3. Start by adding some staff, patients, and equipment data.
4. Generate a schedule for a specific date.
5. View the generated schedule and resource allocation.

## Testing

Run the tests using:

```
python -m unittest discover tests
```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- This project is part of the Outpatient Department Planning System (OPDPS) initiative.
- Thanks to all contributors and users of this MVP.