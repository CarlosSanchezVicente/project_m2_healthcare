# IMPORTS
import numpy as np
import pandas as pd


# MAIN FUNCTIONS
def read_data(path):
    return pd.read_csv(path, sep=',')