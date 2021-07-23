"""
VIEWS FILE FOR MANAGE USER

PEP8 exeptions: (flake8) E722 - Do not use bare 'except'
"""
import os
import requests

from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from purbeurre.settings import MEDIA_URL

from webapp.models import Save
from usermanage.models import Image
from usermanage.forms import RegistrationForm, ImageForm
from webapp.modules.tools.builder import build_response


def legal_notices(request):
    return render(request, 'legal_notices.html')


def signin(request):
    # IF USER COME FROM result.html AND WASN'T CONNECTED
    from_result = 0
    code = request.GET.get('query')

    if code:
        from_result = 1
    
    # IF USER IS AUTH, REDIRECT TO account.html - "/account"
    if request.user.is_authenticated:
        return redirect("account")

    # METHOD TO CONNECT USER
    data = {"id": 1}

    if request.method == "POST":
        email_or_username = request.POST.get('username')
        form = None
        user = None
        if ("@" and ('.fr' or '.com')) in email_or_username:
            user = User.objects.get(email__iregex=f'{email_or_username}')
            username = user.username
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
        else:
            form = AuthenticationForm(request, request.POST)
        # IF EMAIL IS VALID AND PASSWORD CORRECT
        if user is not None:
            login(request, user)
        # IF FORM IS VALID
        elif form is not None:
            if form.is_valid():
                login(request, form.user_cache)
            
        if request.user.is_authenticated:
            # REDIRECT TO ACCOUNT IF DIDN'T COME FROM /result
            if not from_result:
                return redirect("index")
            # REDIRECT TO RESULT IF IT IS
            elif from_result:
                return HttpResponseRedirect(f"/result?query={code}")
        # IF FORM IS NOT VALID
        # TO ADD WARNINGS "wrong_id"
        data["id"] = 0
        # METHOD TO DISPLAY ACCOUNT

    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', data)


def signup(request):
    data = {"form": RegistrationForm(), "mail": 1}
    
    if request.method == "POST":

        cgu_accepted = request.POST.get('scales')
        data["mail"] = 0
        data["address"] = request.POST.get('mail')
        if cgu_accepted:
            if len(request.POST.get('password')) >= 8:
                if request.POST.get('password') == request.POST.get('password2'):

                    if len(request.POST.get('username')) >= 2:
                        try:
                            User.objects.create_user(
                                username=request.POST.get('username'),
                                password=request.POST.get('password'),
                                email=request.POST.get('mail'),
                                first_name=request.POST.get('first_name'),
                                last_name=request.POST.get('last_name')
                            )
                            return redirect("signin")
                        except:
                            data['status'] = 'fail_to_created_user'
                            return render(request, 'signup.html', data)
                    else:
                        data['status'] = 'username_to_short'
                else:
                    data['status'] = 'pw_not_pw2'
            else:
                data['status'] = 'to_short_pw'
        else:
            data['status'] = 'not_cgu'

        return render(request, 'signup.html', data)

    elif request.method == "GET":
        mail = request.GET.get('mail')
        if mail:
            try:
                is_exist = User.objects.get(email=mail)
                data = {"form": RegistrationForm(), "mail": 1, "exist": 1}
            except:
                data = {"form": RegistrationForm(), "mail": 0, 'address': f'{mail}'}

    return render(request, 'signup.html', data)


@login_required
def log_out(request):
    logout(request)
    return redirect("index")


@login_required
def account(request):

    username = request.user.first_name + request.user.last_name

    # METHOD TO DISPLAY ACCOUNT
    if request.method == 'GET':
        # METHOD TO DISPLAY BLOC LAST SUBSTITUTE
        products = Save.objects.filter(user=request.user.email).order_by('-save_id')
        list_substitution = []
        if len(products) == 0:
            list_substitution = 0

        else:
            if len(products) >= 1:
                # products = products[0:3]
                product = products[0]
            dict_product = {}

            """ TO DISPLAY MORE ONE 
            for product in products: """
            prod_code = product.product_substitued
            prod_data = build_response(prod_code, "code")
            sub_code = product.substitute
            sub_data = build_response(sub_code, "code")

            dict_product = {'old': prod_data, 'new': sub_data}
            list_substitution.append(dict_product)

        # METHOD TO DISPLAY IMAGE
        url = f"{MEDIA_URL}{username}.png"
        img_prof = requests.get(url)
        if img_prof.status_code == 200:
            is_exist = username
        else:
            is_exist = 0
        
        # RETURN
        data = {
            "form": ImageForm(),
            "img": is_exist,
            "products": list_substitution,
            "media_location": MEDIA_URL,
        }
        return render(request, 'account.html', data)

    # METHOD TO UPLOAD AN IMAGE
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form.instance.title == username
        if form.is_valid():
            # IF USER SAID GOOD NAME
            if f"{username}.png" == form.instance.image:
                form.save()
            return render(request, 'account.html', {"media_location": MEDIA_URL, "img": username})
        else:
            return render(request, 'account.html', {"media_location": MEDIA_URL})


@login_required
def delete_user(request):
    if request.method == "GET":
        user = User.objects.get(email__iregex=f"{ request.user.email }")
        user.delete()
        datas = Save.objects.filter(user__iregex=f"{ request.user.email }")
        datas.delete()
        return redirect("index")


@csrf_exempt
@login_required
def modif_user(request):
    if request.method == "POST":
        user = User.objects.get(email__iregex=f"{ request.user.email }")
        if request.POST.get('username') != "":
            user.username = request.POST.get('username')
        if request.POST.get('first_name') != "":
            user.first_name = request.POST.get('first_name')
        if request.POST.get('last_name') != "":
            user.last_name = request.POST.get('last_name')
        if request.POST.get('password') != "":
            user.password = request.POST.get('password')
        user.save()
        return HttpResponseRedirect("/signin")


def pdf_view(request):
    file = request.GET.get('query')

    with open(f'webapp/static/assets/media/pdf/{file}.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=conditions_générales_dutilisations.pdf'
        return response


def error_400(request, exception, **kwargs):
    return render(request, 'error/400.html')


def error_403(request, exception, **kwargs):
    return render(request, 'error/403.html')


def error_404(request, exception):
    return render(request, 'error/404.html')


def error_500(request, *args, **kwargs):
    return render(request, 'error/500.html')