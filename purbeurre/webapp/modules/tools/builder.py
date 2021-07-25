"""
BUILDER FILE
to build response for HTML ressources
"""

from webapp.models import Product
from webapp.modules.api.api_manager import get_datas
from webapp.modules.tools.wrapper import wrap_datas

list_of_nutr = ["a", "b", "c", "d", "e", "x"]


def build_response(data, target, *args):

    # *************** FOR SELECTION ****************
    if target == 'code':
        with_nutr = 0
        for arg_ in args:
            with_nutr = arg_

        try:
            # Search product by code in database
            product_data = Product.objects.get(code=data)
            return wrap_datas(product_data, 'db', with_nutr)

        except:   # noqa
            # Search product by api openfoodfacts
            product_data = get_datas(f'{data}', target, 1)
            if product_data:
                return wrap_datas(product_data, 'api', with_nutr)

    elif target == 'name':

        # Search product by name in database
        product_data = Product.objects.filter(product_name__iregex=data)
        products_list = []
        # If there are less 6 products
        if len(product_data) >= 6:
            # Add 6 products to list and return it
            for product in product_data:
                # Set 1 to add nutriments
                products_list.append(wrap_datas(product, 'db', 0))
                if len(products_list) == 6:
                    return products_list
        else:
            # Get 6 products by api openfoodfacts
            product_data = get_datas(f'{data}', target, 6)
            # If they are datas
            if product_data:
                # Add 6 products to list and return it
                for product in product_data:
                    # Set 1 to add nutriments
                    products_list.append(
                        wrap_datas({"product": product}, 'api', 0)
                    )
                    if len(products_list) == 6:
                        return products_list

    # *************** FOR RESULT ****************
    elif target == 'category':

        old_ref = ""
        for arg_ in args:
            if arg_ in list_of_nutr:
                old_nutr = arg_
                old_ref = list_of_nutr.index(old_nutr)

        # Search product by category in database
        product_data = Product.objects.filter(category__iregex=f'{data}')
        products_list = []
        # If there are more than 6 products
        if len(product_data) >= 6:
            # Add 6 products to list and return it
            for product in product_data:

                if old_ref:
                    product_dict = wrap_datas(product, 'db', 0)
                    if list_of_nutr.index(
                        product_dict["nutriscore"]
                    ) <= old_ref:
                        products_list.append(product_dict)
                # Set 1 to add nutriments
                else:
                    products_list.append(wrap_datas(product, 'db', 0))

                if len(products_list) == 6:
                    return products_list

        # Search product by category by api
        else:
            product_data = get_datas(data, target, 6)

            if product_data:
                products_list = []
                for product in product_data:
                    if old_ref:
                        product_dict = wrap_datas(
                            {"product": product},
                            'api',
                            0
                        )
                        if product_dict["nutriscore"]:
                            if list_of_nutr.index(
                                product_dict["nutriscore"]
                            ) < old_ref:
                                products_list.append(product_dict)

                    else:
                        products_list.append(
                            wrap_datas(
                                {"product": product},
                                'api',
                                0
                            )
                        )

                    if len(products_list) == 6:
                        return products_list
                return products_list

    elif target == 'sub_category':
        return get_datas(data, target, 0)
