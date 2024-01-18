# IMPORTS
import numpy as np
import pandas as pd


# MAIN FUNCTIONS
def change_format(df):
    # Change the format of dates such as 'Date of Admission' and 'Discharge Date'.
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    return df