# IMPORTS
import numpy as np
import pandas as pd


# MAIN FUNCTIONS
def change_format(df):
    """Summary: function to transform and change the forma of some columns

    Args:
        df (dataframe): dataframe with the data to transform

    Returns:
        df (dataframe): dataframe transformed
    """
    # Change the format of dates such as 'Date of Admission' and 'Discharge Date'.
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    return df