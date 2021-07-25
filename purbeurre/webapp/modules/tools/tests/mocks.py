""" CONSTANTE MOCK """
from decimal import Decimal


MOCK_PROD_RESP = {
    "code": "3017620422003",
    "product_url": "http://world.openfoodfacts.org/product/3017620422003",
    "nutriscore": "e",
    "product_name": "Nutella t.400",
    "category": "Pates a tartiner",
    "product_img": "https://images.openfoodfacts.org/images/products/301/762/042/2003/front_fr.270.400.jpg",   # noqa
}

MOCK_FULL_PROD_RESP = {
    "code": "3017620422003",
    "product_url": "http://world.openfoodfacts.org/product/3017620422003",
    "nutriscore": "e",
    "product_name": "Nutella t.400",
    "category": "Pates a tartiner",
    "product_img": "https://images.openfoodfacts.org/images/products/301/762/042/2003/front_fr.270.400.jpg",   # noqa
    "energy_100g": 2252,
    "energy_unit": "kJ",
    "proteins_100g": 6.3,
    "fat_100g": 30.9,
    "saturated_fat_100g": 10.6,
    "carbohydrates_100g": 57.5,
    "sugars_100g": 56.3,
    "fiber_100g": 0,
    "salt_100g": 0.107
}

MOCK_NAME = [{'code': '3017620422003', 'product_url': 'http://world.openfoodfacts.org/product/3017620422003', 'nutriscore': 'e', 'product_name': 'Nutella t.400', 'category': 'Pates a tartiner', 'product_img': 'https://images.openfoodfacts.org/images/products/301/762/042/2003/front_fr.270.400.jpg'}, {'code': '3017620425035', 'product_url': 'http://world.openfoodfacts.org/product/3017620425035', 'nutriscore': 'e', 'product_name': 'Nutella t.1000', 'category': 'Pates a tartiner', 'product_img': 'https://images.openfoodfacts.org/images/products/301/762/042/5035/front_fr.315.400.jpg'}, {'code': '8000500310427', 'product_url': 'http://world.openfoodfacts.org/product/8000500310427', 'nutriscore': 'e', 'product_name': 'Nutella biscuits', 'category': 'Kekse', 'product_img': 'https://images.openfoodfacts.org/images/products/800/050/031/0427/front_fr.97.400.jpg'}, {'code': '3017620420047', 'product_url': 'http://world.openfoodfacts.org/product/3017620420047', 'nutriscore': 'e', 'product_name': 'Nutella', 'category': 'Pates a tartiner', 'product_img': 'https://images.openfoodfacts.org/images/products/301/762/042/0047/front_fr.140.400.jpg'}, {'code': '3017620421006', 'product_url': 'http://world.openfoodfacts.org/product/3017620421006', 'nutriscore': 'e', 'product_name': 'Nutella t.750', 'category': 'Pates a tartiner', 'product_img': 'https://images.openfoodfacts.org/images/products/301/762/042/1006/front_fr.225.400.jpg'}, {'code': '3017620429484', 'product_url': 'http://world.openfoodfacts.org/product/3017620429484', 'nutriscore': 'e', 'product_name': 'Nutella t825 new ean 2013', 'category': 'Pates a tartiner', 'product_img': 'https://images.openfoodfacts.org/images/products/301/762/042/9484/front_fr.280.400.jpg'}]      # noqa
MOCK_CATEGORY = [{'code': '8001505005592', 'product_url': 'http://world.openfoodfacts.org/product/8001505005592', 'nutriscore': 'd', 'product_name': 'Nocciolata pâte à tartiner au ', 'category': 'Pates a tartiner', 'product_img': 'https://images.openfoodfacts.org/images/products/800/150/500/5592/front_fr.113.400.jpg'}, {'code': '8001505005707', 'product_url': 'http://world.openfoodfacts.org/product/8001505005707', 'nutriscore': 'd', 'product_name': 'Nocciolata', 'category': 'Pates a tartiner', 'product_img': 'https://images.openfoodfacts.org/images/products/800/150/500/5707/front_fr.128.400.jpg'}]      # noqa

MOCK_PROD_FOR_DB = {'product_name': 'Tpp orange sans pulpe pet 1l', 'category': "jus d'orange", 'product_img': 'https://images.openfoodfacts.org/images/products/350/211/000/9449/front_fr.112.400.jpg', 'nutriscore': 'c', 'product_url': 'http://world.openfoodfacts.org/product/3502110009449', 'code': '3502110009449'}     # noqa
MOCK_FULL_PROD_FOR_DB = {'product_name': 'Tpp orange sans pulpe pet 1l', 'category': "jus d'orange", 'product_img': 'https://images.openfoodfacts.org/images/products/350/211/000/9449/front_fr.112.400.jpg', 'nutriscore': 'c', 'product_url': 'http://world.openfoodfacts.org/product/3502110009449', 'code': '3502110009449', 'energy_100g': Decimal('182.00'), 'energy_unit': 'kJ', 'proteins_100g': Decimal('0.80'), 'fat_100g': Decimal('0.00'), 'saturated_fat_100g': Decimal('0.00'), 'carbohydrates_100g': Decimal('8.90'), 'sugars_100g': Decimal('8.90'), 'fiber_100g': Decimal('0.60'), 'salt_100g': Decimal('0.00')}     # noqa
