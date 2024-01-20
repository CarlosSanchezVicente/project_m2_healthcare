# IMPORTS
import numpy as np
import pandas as pd

# IMPORT FUNCTIONS FROM MODULES
from modules import read_data as rd
from modules import clean_data as cd
from modules import normalization as n
from modules import processing_tables as pt
from modules import store_tables as st

# DEFINITION
path = '../data/raw_data/healthcare_dataset.csv'
path_store = '../data/normalized_data/df_patients.csv'


# MAIN FUNCTION
def main():
    # Read data
    df = rd.read_data(path)
    
    # Clean data
    df = cd.change_format(df)
    
    # Transform the dataframe
    df = n.create_new_columns(df)
    # Create the normalized dataframes
    df_patients = n.create_patients_df(df)
    df_hospital = n.create_hospital_df(df)
    df_doctors = n.create_doctors_df(df)
    df_medication = n.create_medication_df(df)
    df_provider = n.create_provider_df(df)
    df_date = n.create_date_df(df_patients)

    # Store data
    st.store_csv(df_patients, df_hospital, df_doctors, df_medication, df_provider, df_date, path_store)


# MAIN EXECUTION
if __name__ == '__main__':
    result = main()
    print(result)