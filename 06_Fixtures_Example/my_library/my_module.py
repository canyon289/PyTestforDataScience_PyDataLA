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


def drop_list_item(some_list):
    """Drop the last item off the list"""
    some_list.pop()
    return 


def add_item_to_list(some_list):
    """Add some item to the end of the list"""
    some_list.append(10)
    return



