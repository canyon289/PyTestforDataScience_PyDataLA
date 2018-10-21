"""
Lets fake a request
"""
import requests


def get_data_from_api():
    """Go to the internet and get something from an api"""
    url = "https://some_really_fake_website_that_doesnt_exist.com"
    response = requests.get(url)
    print(response)
    return response


def get_json_from_response():
    url = "https://some_really_fake_website_that_doesnt_exist.com"
    response = requests.get(url)
    json = response.json()
    return json
