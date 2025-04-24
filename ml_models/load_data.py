# load_data.py

import pandas as pd


def load_data(file_path):
    """
    Load dataset from a CSV file.

    :param file_path: Path to the CSV file
    :return: Pandas DataFrame
    """
    return pd.read_csv(file_path)
