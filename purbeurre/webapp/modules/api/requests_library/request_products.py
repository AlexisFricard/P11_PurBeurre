"""
REQUEST PRODUCTS BY NAME
"""
import requests

import webapp.modules.api.analysis.analysis_data as ad
analysis = ad.Analyze_data()


def openfoodfact_terms(terms, number):

    page = 1

    """ BUILD URL """
    url_begin = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms='
    url_end = '&search_simple=1&action=process&json=1'
    url_page = f'&page={page}'
    
    url = f"{url_begin}{terms}{url_end}{url_page}"

    """ REQUEST """
    datas = requests.get(url).json()

    # Add product to a list
    products_list = []
    for product in datas["products"]:
        products_list.append(product)
        if len(products_list) == number + 2:
            return products_list


def openfoodfact_categorie(category, number):

     # BUILD URL FOR REQUEST
    url_begin = "https://fr.openfoodfacts.org/categorie/"
    parameter = f"{category}"
    url_end = "&sort_by=nutriscore_score&json=1"
    url = f"{url_begin}{parameter}{url_end}"

    """ REQUEST """
    datas = requests.get(url).json()
    products_list = []
    for product in datas["products"]:
        products_list.append(product)
        if len(products_list) == number:
            return products_list

