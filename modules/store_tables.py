# IMPORTS
import numpy as np
import pandas as pd


# MAIN FUNCTIONS
def store_csv(df_patients, df_hospital, df_doctors, df_medication, df_provider, df_date):
    # Save df_patients
    df_patients.to_csv('../data/normalized_data/df_patients.csv', index=False)

    # Save df_hospital
    df_hospital.to_csv('../data/normalized_data/df_hospital.csv', index=False)

    # Save df_doctors
    df_doctors.to_csv('../data/normalized_data/df_doctors.csv', index=False)

    # Save df_medication
    df_medication.to_csv('../data/normalized_data/df_medication.csv', index=False)

    # Save df_provider
    df_provider.to_csv('../data/normalized_data/df_provider.csv', index=False)

    # Save df_date
    df_date.to_csv('../data/normalized_data/df_date.csv', index=False)