"""
VIEWS FILE MANAGE PRODUCTS
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from webapp.modules.tools.clean_sentence import clean_query
from webapp.modules.tools.builder import build_response
from webapp.modules.psql.db_manager import save_research, del_research
from webapp.modules.psql.db_manager import add_data
from webapp.models import Save, Product


def index(request):
    return render(request, 'index.html')


def selection(request):

    if request.method == "POST":

        # Get user input
        query = request.POST.get('user_text')
        query_clnd = clean_query(query)

        # Research error
        if query_clnd is None:
            return redirect('index')

        # Input is bar code --> result
        elif type(query_clnd) == type(int()):
            data = {}
            data['prod'] = build_response(query_clnd, 'code')
            sub_category = build_response(data['prod']['product_url'], 'sub_category')
            data['sub'] = build_response(sub_category, 'category')
            return render(request, 'results.html', data)

        # Input is a product name --> selection
        else:
            data = {}
            data['products'] = build_response(query_clnd, 'name')
            return render(request, 'selection.html', data)

    else:
        return redirect('index')


def result(request):

    if request.method == "GET":

        code = request.GET.get('query')
        compare_code = request.GET.get('compare')

        datas = {}
        if code:
            datas['prod'] = build_response(int(code), "code")
            sub_category = build_response(datas['prod']['product_url'], 'sub_category')
            prod_categ = datas['prod']['category']
            prod_nutr = datas['prod']['nutriscore']
            datas['sub1'] = build_response(sub_category, 'category', prod_nutr)
            if len(datas['sub1']) < 6:
                datas['sub1'] = build_response(prod_categ, 'category', prod_nutr)
            if datas['sub1']:
                if len(datas['sub1']) >= 6:
                    datas['sub2'] = datas['sub1'][0:3]
                    datas['sub1'] = datas['sub1'][3:6]
        
        if compare_code:
            datas['comp_prod'] = build_response(compare_code, "code")

        return render(request, 'results.html', datas)

@login_required
def myfood(request):

    products = Save.objects.filter(user__iregex=f"{request.user.email}")
    dict_product = {}
    list_substitution = []

    for product in products:
        prod_code = product.product_substitued
        prod_data = build_response(prod_code, "code")
        sub_code = product.substitute
        sub_data = build_response(sub_code, "code")

        dict_product = {'old': prod_data, 'new': sub_data}
        list_substitution.append(dict_product)

    datas = {"substitutions": list_substitution}
    return render(request, "myfood.html", datas)

@login_required
def save(request):

    if request.method == "GET":
        data = request.GET.get('query')
        datas = data.replace(",", " ").split()

        datas.append(request.user.email)
        save_research(datas)

        prod_exist = Product.objects.filter(code=f"{datas[0]}")
        sub_exist = Product.objects.filter(code=f"{datas[1]}")
        if not prod_exist:
            add_data(build_response(datas[0], "code"))
        else:
            print('prod 1 exist')
        if not sub_exist:
            add_data(build_response(datas[1], "code"))
        else:
            print('prod 2 exist')

        return redirect('myfood')

@login_required
def del_sub(request):
    if request.method == "GET":
        data = request.GET.get('query')
        datas = data.replace(",", " ").split()

        if request.user.is_authenticated:
            datas.append(request.user.email)
            del_research(datas)
            return redirect('myfood')

        else:
            return redirect('signin')