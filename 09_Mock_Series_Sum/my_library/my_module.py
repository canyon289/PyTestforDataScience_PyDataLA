"""Check if dataframe is huge"""
import pandas as pd


def is_sum_of_series_big(series):

    # Lets check if this dataframe has over a million rows
    if series.sum() > 1000:
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = pd.Series([1000, 1000])
    print(s1)
    print(is_sum_of_series_big(s1))

    s2 = pd.Series([1, 1])
    print(s2)
    print(is_sum_of_series_big(s2))

