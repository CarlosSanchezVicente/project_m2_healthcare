# IMPORTS
import numpy as np
import pandas as pd


# MAIN FUNCTIONS
def store_csv(df_patients, df_hospital, df_doctors, df_medication, df_provider, df_date, path_store):
    """Summary: function to store each dataframe in diferent .csv files.

    Args:
        df_patients (dataframe): dataframe with patient data. It will be the fact table.
        df_hospital (dataframe): dataframe with hospital data. It will be the dimension table.
        df_doctors (dataframe): dataframe with doctors data. It will be the dimension table.
        df_medication (dataframe): dataframe with medication data. It will be the dimension table.
        df_provider (dataframe): dataframe with insurance provider data. It will be the dimension table.
        df_date (dataframe): dataframe with date data. It will be the dimension table.
    """
    # Save df_patients
    df_patients.to_csv(path_store, index=False)

    # Save df_hospital
    df_hospital.to_csv(path_store, index=False)

    # Save df_doctors
    df_doctors.to_csv(path_store, index=False)

    # Save df_medication
    df_medication.to_csv(path_store, index=False)

    # Save df_provider
    df_provider.to_csv(path_store, index=False)

    # Save df_date
    df_date.to_csv(path_store, index=False)