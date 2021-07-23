"""
RESPONSE TO GIVEN CODE
"""
import requests


def openfoodfact_api(code):

    """ BUILD URL """
    url_begin = 'http://world.openfoodfacts.org/api/v0/product/'
    url_end = '.json'

    url = f"{url_begin}{code}{url_end}"

    """ REQUEST """
    data = requests.get(url).json()
    return data
