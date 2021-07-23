

def wrap_datas(datas, dict_from, with_nutriments):

    # **************************************************************
    # *********************** Primary datas ************************
    # **************************************************************
    product_datas = {}

    # The dict's from the database
    if dict_from == 'db':

        for row in datas:
            product_datas["product_name"] = row.product_name
            product_datas["category"] = row.category
            product_datas["product_img"] = row.product_img
            product_datas["nutriscore"] = row.nutriscore
            product_datas["product_url"] = row.product_url
            product_datas["code"] = row.code
    
    # The dict's from an api requests
    elif dict_from == 'api':

        # ******************************************
        # ***************** Code *******************
        product_datas["code"] = (
            datas["product"].get("_id")
        )
        # ************** Product url ***************
        product_datas["product_url"] = (
            f"http://world.openfoodfacts.org/product/{product_datas['code']}"
        )
        # ******************************************
        # *************** Nutriscore ***************
        product_datas["nutriscore"] = (
            datas["product"].get("nutriscore_grade", None)
        )
        if product_datas['nutriscore'] == None:
            product_datas['nutriscore'] = 'x'
        # ******************************************
        # ************** Product name **************
        try:
            product_datas['product_name'] = (
                datas['product']['abbreviated_product_name_fr']
            )
        except KeyError:
            try:
                product_datas['product_name'] = (
                    datas['product']['product_name_fr']
                )
            except KeyError:
                product_datas['product_name'] = (
                    datas['product']['product_name']
                )
        if len(product_datas['product_name']) > 31:
            product_datas['product_name'] = (
                product_datas['product_name'][0:30]
            )
        product_datas['product_name'] = product_datas["product_name"].capitalize()
        # ******************************************
        # *********** Product categorie ************
        is_fr_category = 0

        if datas['product']['categories_hierarchy']:

            for categorie in datas['product']['categories_hierarchy']:
                if categorie.startswith("fr:"):
                    fr_category = categorie.replace("fr:", "")
                    is_fr_category = 1

            if is_fr_category:
                product_datas['category'] = fr_category

        if not is_fr_category:
            try:
                list_of_categ = datas['product'].get('categories_old').split(',')
                try:
                    temp_category = list_of_categ[-1]
                    temp_category = temp_category.split(" ")

                except TypeError:
                    temp_category = list_of_categ[0]
                    temp_category = temp_category.split(" ")

                if len(temp_category) > 4:
                    while len(temp_category) != 4:
                        data = temp_category[-1]
                        temp_category.remove(data)

                product_datas['category'] = ' '.join(temp_category)

            except AttributeError:
                product_datas['category'] = "Unfound"
        
        if "-" in product_datas['category']:
            product_datas['category'] = (
                product_datas['category'].replace("-", " ").capitalize()
            )
        # ******************************************
        # ************** Product image *************
        try:
            product_datas["product_img"] = (
                datas["product"]["selected_images"]["front"]["display"]["fr"]
            )
        except KeyError:
            product_datas["product_img"] = (
                datas["product"].get("image_front_url")
            )
        if product_datas['product_img'] == None:
            product_datas['product_img'] = '/static/assets/img/unfound.jpg'
    # *****************************************************************
    # *********************** Nutriments datas ************************
    # *****************************************************************
    if with_nutriments and (dict_from == "api"):
        
        product_datas["energy_100g"] = (
            datas["product"]["nutriments"].get("energy_100g", None)
        )
        product_datas["energy_unit"] = (
            datas["product"]["nutriments"].get("energy_unit", None)
        )
        product_datas["proteins_100g"] = (
            datas["product"]["nutriments"].get("proteins_100g", None)
        )
        product_datas["fat_100g"] = (
            datas["product"]["nutriments"].get("fat_100g", None)
        )
        product_datas["saturated_fat_100g"] = (
            datas["product"]["nutriments"].get("saturated-fat_100g", None)
        )
        product_datas["carbohydrates_100g"] = (
            datas["product"]["nutriments"].get("carbohydrates_100g", None)
        )
        product_datas["sugars_100g"] = (
            datas["product"]["nutriments"].get("sugars_100g", None)
        )
        product_datas["fiber_100g"] = (
            datas["product"]["nutriments"].get("fiber_100g", 0)
        )
        product_datas["salt_100g"] = (
            datas["product"]["nutriments"].get("salt_100g", None)
        )

    if with_nutriments and (dict_from == "db"):
        print("form db nutriments")
    # *****************************************************************
    # ************************   RETURN   *****************************
    # *****************************************************************
    return product_datas