"""Check if dataframe is huge"""


def is_dataframe_big(dataframe):

    # Lets check if this dataframe has over a million rows
    if dataframe.shape[0] > 1000000:
        return True
    else:
        return False
