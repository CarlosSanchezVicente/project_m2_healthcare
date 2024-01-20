# IMPORTS
import numpy as np
import pandas as pd


# MAIN FUNCTIONS
def read_data(path):
    """Summary: function to read csv

    Args:
        path (string): path of the file

    Returns:
        df (dataframe): dataframe with the data
    """
    return pd.read_csv(path, sep=',')