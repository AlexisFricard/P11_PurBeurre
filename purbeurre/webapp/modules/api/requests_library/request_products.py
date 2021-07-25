"""
REQUEST PRODUCTS BY NAME
"""
import requests


def openfoodfact_terms(terms, number):

    page = 1

    # BUILD URL
    url_begin = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms='
    url_end = '&search_simple=1&action=process&json=1'
    url_page = f'&page={page}'

    url = f"{url_begin}{terms}{url_end}{url_page}"

    # REQUEST
    datas = requests.get(url).json()

    # RETURN A LIST
    products_list = []
    for product in datas["products"]:
        products_list.append(product)
        if len(products_list) == number:
            return products_list


def openfoodfact_categorie(category, number):

    # BUILD URL STAGE-1
    url_begin = "https://fr.openfoodfacts.org/categorie/"
    parameter = f"{category}"
    url_end = "&sort_by=nutriscore_score"
    url = f"{url_begin}{parameter}{url_end}"

    # REQUEST TO GET FINAL & VALID URL
    datas = requests.get(url)

    # BUILD URL STAGE-2
    if datas.url == url:
        # NO CHANGE DETECTED
        url = f"{url_begin}{parameter}.json{url_end}"
    elif datas.url != url:
        # CHANGE DETECTED
        url = datas.url + ".json" + url_end

    # REQUEST
    datas = requests.get(url).json()

    # RETURN A LIST
    products_list = []
    for product in datas["products"]:
        products_list.append(product)
        if len(products_list) == number:
            return products_list
