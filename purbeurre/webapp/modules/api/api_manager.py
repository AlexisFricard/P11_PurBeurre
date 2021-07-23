"""
API RESEARCH
OPENFOODFACT

PEP8 exeptions: (flake8) E501 - line (9,10) too long * 2
"""


from webapp.modules.api.requests_library.request_html_categ import (
    html_categorie_from_product_url
)
from webapp.modules.api.requests_library.request_products import (
    openfoodfact_terms, openfoodfact_categorie
)
from webapp.modules.api.requests_library.request_code import (
    openfoodfact_api
)
from webapp.modules.tools.display import display_loading, display_start


def get_datas(product_ref, target_ref, numb_of_prod):

    if target_ref == 'code':
        return openfoodfact_api(product_ref)

    if target_ref == 'name':
        return openfoodfact_terms(product_ref, numb_of_prod)

    if target_ref == 'sub_category':
        return html_categorie_from_product_url(product_ref)

    if target_ref == 'category':
        return openfoodfact_categorie(product_ref, numb_of_prod)

def get_products(target, number, params, data):

    """ TO FILL PRODUCTS IN DB """
    if target == 'products':

        """ ALL PRODUCTS """
        if params == 'all':

            if params == 'all':
                """ GET WORK DATAS """
                categories = query_categories()
                """ INITIALYZE STATE """
                state = 0
                display_start()
                """ FOR EACH CATEGORIE IN LIST """
                for categorie in categories:
                    """ GET PRODUCTS """
                    state += (number/nb_categories)
                    display_loading(state, number)

