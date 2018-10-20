"""
Lets make an adder function
"""
import pandas as pd


def load_data_frame_from_sql_and_add_2():
    """We want to load a dataframe from SQL and add two"""
    df = pd.read_sql("Some Table", "some_conn")

    new_df = df + 2
    return new_df
