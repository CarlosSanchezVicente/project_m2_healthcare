# IMPORTS
import numpy as np
import pandas as pd
import random


# AUXILIARY FUNCTIONS
def create_stay_columns(df):
    # Column with length of hospital stay
    df['Length Stay'] = df['Discharge Date'] - df['Date of Admission']  
    return df


def create_id_columns(df, name):
    # Create a new column with the id_hospital
    # Get unique values from the column 'Hospital'.
    unique = df[name].unique()

    # Create a new DataFrame with the unique values of 'Hospital'.
    df = pd.DataFrame({name: unique})

    # Add a new column 'id_hospital' with unique identifiers
    id_name = f"id_{name}"
    df[id_name] = range(len(df))

    # Merge the two DataFrames using the column 'Hospital'.
    df = pd.merge(df, df, on=name, how='left')

    return df



# MAIN FUNCTIONS
def create_new_columns(df):
    # Function to create stay columns
    df = create_stay_columns(df)

    # Function to create id columns
    list = ['hospital', 'doctors', 'provider', 'medication']
    for name in list:
        df = create_id_columns(df, name)
    
    # Create a new column with the id_patient
    df['id_patient'] = df.reset_index().index

    return df


def create_patients_df(df):
    # Create patients dataframe
    columns_patients = ['id_patient','Name', 'Age', 'Gender', 'Blood Type', 'Medical Condition', 'Date of Admission',
                        'Discharge Date', 'Length Stay', 'Room Number', 'Admission Type', 'Test Results', 'Billing Amount',
                        'id_hospital', 'id_doctors', 'id_medication', 'id_provider']
    df_patients = df[columns_patients].copy()

    # Change the names of some columns in df_patients
    new_column_names = {'Name': 'name_patient', 
                        'Age': 'age', 
                        'Gender': 'gender', 
                        'Blood Type': 'blood_type', 
                        'Medical Condition': 'medical_condition', 
                        'Date of Admission': 'date_admission',
                        'Discharge Date': 'date_discharge', 
                        'Length Stay': 'hospital_stay', 
                        'Room Number': 'room_number', 
                        'Admission Type': 'admission_type', 
                        'Test Results': 'test_result', 
                        'Billing Amount': 'billing_amount'}

    df_patients = df_patients.rename(columns=new_column_names)

    return df_patients


def create_hospital_df(df):
    # Change the order of columns
    columns_hospital = ['id_hospital', 'Hospital']
    df_hospital = df_hospital[columns_hospital]

    # Change the names of some columns in df_hospital
    new_column_names = {'Hospital': 'name_hospital'}
    df_hospital = df_hospital.rename(columns=new_column_names)

    # Create new column with state
    # List of EEUU
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
            'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
            'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
            'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
            'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
            'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
            'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

    # Assign random statuses to each hospital
    df_hospital['state'] = [random.choice(states) for state in range(len(df_hospital))]

    return df_hospital


def create_doctors_df(df):
    # Change the order of columns
    columns_doctors = ['id_doctors', 'Doctor']
    df_doctors = df_doctors[columns_doctors]

    # Change the names of some columns in df_hospital
    new_column_names = {'Doctor': 'name_doctors'}
    df_doctors = df_doctors.rename(columns=new_column_names)

    # Map medical conditions to specialties
    specialty_map = {
        'Diabetes': 'Endocrinology',
        'Obesity': 'Endocrinology',
        'Asthma': 'Pneumology',
        'Arthritis': 'Rheumatology',
        'Hypertension': 'Cardiology',
        'Cancer': 'Oncology'}

    # Create new column 'medical_specialty' based on 'Medical Condition'.
    df_doctors['medical_specialty'] = df['Medical Condition'].apply(lambda x: specialty_map.get(x, ''))

    return df_doctors


def create_medication_df(df):
    # Change the order of columns
    columns_medication = ['id_medication', 'Medication']
    df_medication = df_medication[columns_medication]

    # Change the names of some columns in df_hospital
    new_column_names = {'Medication': 'name_medication'}
    df_medication = df_medication.rename(columns=new_column_names)

    # Add new columns
    new_column = ['medication_type', 'api']

    # Crear la nueva columna 'new_column'
    df_medication['medication_type'] = ['acetylsalicylic acid', 'atorvastatin', '6-aminopenicillanic acid', 'paracetamol', 
                                        'Ibuprofen']
    df_medication['api'] = ['salicylates', 'statins', 'antibiotic', 'analgesic and antipyretic (NSAID)', 
                            'anti-inflammatory (NSAID)']
    
    return df_medication


def create_provider_df(df):
    # Create the order of columns
    columns_provider = ['id_provider', 'Insurance Provider']
    df_provider = df_provider[columns_provider]

    # Change the names of some columns in df_medication
    new_column_names = {'Insurance Provider': 'name_provider'}
    df_provider = df_provider.rename(columns=new_column_names)

    return df_provider


def create_date_df(df_patients):
    # First, it's necessary create a column with years only. This will be the primary key in the new table in the database
    df_patients['years'] = df_patients['date_admission'].dt.year

    # Sort dataframe
    df_patients_sort = df_patients.sort_values(by='date_admission')

    # Create the new DataFrame 'date'
    date_data = {
        'years': sorted(df_patients_sort['years'].unique()),
        'start_date': pd.to_datetime(df_patients_sort['date_admission']).min(),
        'end_date': pd.to_datetime(df_patients_sort['date_discharge']).max() + pd.DateOffset(days=1),  # Agregar un día
    }

    df_date = pd.DataFrame(date_data)

    # Change start and end dates of the fiscal year
    df_date['start_date'] = df_date['start_date'].apply(lambda x: x.replace(month=11, day=1))
    df_date['end_date'] = df_date['end_date'].apply(lambda x: x.replace(month=10, day=30))

    # Create the column 'fiscal_year'
    df_date['fiscal_year'] = df_date['years'].astype(str) + ' - ' + (df_date['years'] + 1).astype(str)

    return df_date