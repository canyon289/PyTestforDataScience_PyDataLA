"""
Some module with functionality
"""
import time


def load_data():
    """
    Sometimes in our data science code we have functions that take
    a long time. Common are loading data or fitting a machine learning model,
    """
    time.sleep(3)

    # End result is always the same though
    return 5
