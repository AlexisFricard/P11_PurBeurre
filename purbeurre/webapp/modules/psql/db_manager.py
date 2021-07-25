""" DB MANAGER """

from webapp.models import Product, Nutriment, Save


def add_data(prod_dict):

    Product.objects.create(
        product_name=prod_dict.get("product_name"),
        product_url=prod_dict.get("product_url"),
        product_img=prod_dict.get("product_img"),
        category=prod_dict.get("category"),
        nutriscore=prod_dict.get("nutriscore"),
        code=prod_dict.get("code"),
        )

    Nutriment.objects.create(
        code=prod_dict.get("code"),
        energy_100g=prod_dict.get("energy_100g"),
        energy_unit=prod_dict.get("energy_unit"),
        proteins_100g=prod_dict.get("proteins_100g"),
        fat_100g=prod_dict.get("fat_100g"),
        saturated_fat_100g=prod_dict.get("saturated_fat_100g"),
        carbohydrates_100g=prod_dict.get("carbohydrates_100g"),
        sugars_100g=prod_dict.get("sugars_100g"),
        fiber_100g=prod_dict.get("fiber_100g"),
        salt_100g=prod_dict.get("salt_100g"),
        )


def save_research(save_list):

    get_allready_registred = Save.objects.filter(
        user__iregex=f"{save_list[2]}"
        )

    for row in get_allready_registred:
        sub = row.substitute
        prod = row.product_substitued
        if prod == save_list[1]:
            if sub == save_list[0]:
                return

    Save.objects.create(
        user=save_list[2],
        substitute=save_list[0],
        product_substitued=save_list[1],
    )


def del_research(save_list):

    row = Save.objects.filter(
        user=save_list[2],
        substitute=save_list[1],
        product_substitued=save_list[0],
        )
    row.delete()
