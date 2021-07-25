"""
API RESEARCH
OPENFOODFACT
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


def get_datas(product_ref, target_ref, numb_of_prod):

    if target_ref == 'code':
        return openfoodfact_api(product_ref)

    if target_ref == 'name':
        return openfoodfact_terms(product_ref, numb_of_prod)

    if target_ref == 'sub_category':
        return html_categorie_from_product_url(product_ref)

    if target_ref == 'category':
        return openfoodfact_categorie(product_ref, numb_of_prod)
