"""
Test usermanage/views.py
"""
import os
from purbeurre import wsgi  # noqa

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.contrib.sessions.middleware import SessionMiddleware

from usermanage.views import (
    legal_notices,
    signin,
    log_out,
    signup,
    account,
    modif_user
)


class TemplateTest(TestCase):

    def test_legal_notices(self):

        request = RequestFactory().get("/legal_notices")
        view = legal_notices(request)

        assert view.status_code == 200

    def test_signin(self):

        """ TEST 1 """
        request = RequestFactory().get("/signin")
        view = signin(request)
        assert view.status_code == 200

        """ TEST 2 """
        request = RequestFactory().post("/signin")
        request.POST = {
            'username': 'a.fricardpro@gmail.com',
            'password': os.getenv('DB_PWD'),
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()

        view = signin(request)
        assert view.status_code == 302
        assert view.url == "/"

        """ TEST 3 """
        request = RequestFactory().post("/signin")
        request.POST = {
            'username': 'AlexisF',
            'password': os.getenv('DB_PWD'),
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()

        view = signin(request)
        assert view.status_code == 302
        assert view.url == "/"

        """ TEST 4 """
        request = RequestFactory().post("/signin")
        request.GET = {"query": "3330720662002"}
        request.POST = {
            'username': 'a.fricardpro@gmail.com',
            'password': os.getenv('DB_PWD'),
        }

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()

        view = signin(request)
        assert view.status_code == 302
        assert view.url == "/save?query=3330720662002"

    def test_log_out(self):

        request = RequestFactory().post("/log_out")
        request.user = User.objects.get(username="AlexisF")

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        view = log_out(request)

        assert view.status_code == 302
        assert view.url == "/"

    def test_signup(self):

        request = RequestFactory().get("/signup")
        request.GET = {"mail": "aaaa@gmail.com"}
        view = signup(request)
        assert view.status_code == 200

        request = RequestFactory().get("/signup")
        request.GET = {"mail": "a.fricardpro@gmail.com"}
        view = signup(request)
        assert view.status_code == 200

        request = RequestFactory().post(
            "/signup?mail=Test_email%40mail.com&signup_btn="
        )
        request.POST = {
            "scales": "ok",
            "username": "Test_signup",
            "password": "Test_pw78",
            "password2": "Test_pw78",
            "email": "Test_email@mail.com",
            "first_name": "Test_fn",
            "last_name": "Test_ln",
        }
        view = signup(request)
        # 302 - REDIRECT TO Signin to login
        assert view.status_code == 302
        assert view.url == "/signin"

        request.POST = {
            "username": "Test_signup",
            "password": "Test_pw78",
            "password2": "Test_pw78",
            "email": "Test_email@mail.com",
            "first_name": "Test_fn",
            "last_name": "Test_ln",
        }
        view = signup(request)
        # CGU INNACEPTED
        assert view.status_code == 200

        request.POST = {
            "scales": "ok",
            "username": "Test_signup",
            "password": "Test",
            "password2": "Test",
            "email": "Test_email@mail.com",
            "first_name": "Test_fn",
            "last_name": "Test_ln",
        }
        view = signup(request)
        # TO SHORT PWD
        assert view.status_code == 200

        request.POST = {
            "scales": "ok",
            "username": "Test_signup",
            "password": "Testwith8char",
            "password2": "NOTSAMEPASSWORD",
            "email": "Test_email@mail.com",
            "first_name": "Test_fn",
            "last_name": "Test_ln",
        }
        view = signup(request)
        # NOT SAME PWD
        assert view.status_code == 200

        request.POST = {
            "scales": "ok",
            "username": "S",
            "password": "Testwith8char",
            "password2": "Testwith8char",
            "email": "Test_email@mail.com",
            "first_name": "Test_fn",
            "last_name": "Test_ln",
        }
        view = signup(request)
        # USERNAME TO SHORT
        assert view.status_code == 200

    def test_account(self):

        request = RequestFactory().get("/account")
        request.user = User.objects.get(username="AlexisF")
        view = account(request)
        assert view.status_code == 200

    def test_modif_user(self):

        request = RequestFactory().post("/modif_user")
        request.user = User.objects.get(username="AlexisF")
        request.POST = {
            "username": "AlexisF",
            "password": os.getenv('DB_PWD'),
            "email": "a.fricardpro@gmail.com",
            "first_name": "Alexis",
            "last_name": "Fricard",
        }
        view = modif_user(request)
        assert view.status_code == 302
        assert view.url == "/account"
