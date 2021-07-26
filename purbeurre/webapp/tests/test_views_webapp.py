"""
Test webapp/views.py
"""
from purbeurre import wsgi  # noqa

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from webapp.views import (
    index,
    selection,
    result,
    save,
    myfood,
    del_sub
)


class TemplateTest(TestCase):

    def test_index(self):

        request = RequestFactory().get("/index")
        view = index(request)

        assert view.status_code == 200

    def test_selection(self):

        request = RequestFactory().post("/selection")
        request.POST = {"user_text": ""}
        view = selection(request)
        assert view.status_code == 302
        assert view.url == '/'

        request = RequestFactory().post("/selection")
        request.POST = {"user_text": "nutella"}
        view = selection(request)
        assert view.status_code == 200

        request = RequestFactory().post("/selection")
        request.POST = {"user_text": 3017620422003}
        view = selection(request)
        assert view.status_code == 200

        request = RequestFactory().post("/selection")
        request.POST = {"user_text": 135151}
        view = selection(request)
        assert view.status_code == 302

        request = RequestFactory().get("/selection")
        view = selection(request)
        assert view.status_code == 302

    def test_result(self):

        request = RequestFactory().get("/result")
        request.GET = {"query": "3330720662002"}
        view = result(request)
        assert view.status_code == 200

        request = RequestFactory().get("/result")
        request.GET = {
            "query": "3330720662002",
            "compare": "4028491400907"
        }
        view = result(request)
        assert view.status_code == 200

        request = RequestFactory().get("/result")
        request.GET = {
            "query": "3330720662002",
            "matching": "jus d'orange"
        }
        view = result(request)
        assert view.status_code == 200

        request = RequestFactory().get("/result")
        request.GET = {
            "query": "3330720662002",
            "compare": "4028491400907"
        }
        view = result(request)
        assert view.status_code == 200

    def test_save(self):

        # BUILD REQUEST
        request = RequestFactory().get("/save")
        request.GET = {"query": "3330720662002,4028491400907"}

        """ TEST 1 - WITH UNCONNECTED USER """
        request.user = AnonymousUser()
        view = save(request)
        # 302 - REDIRECT TO Signin/
        assert view.status_code == 302
        assert view.url == "/accounts/login/?next=/save"

        """ TEST 2 - WITH CONNECTED USER """
        request.user = User.objects.get(username="dev-purbeurre")
        view = save(request)
        # 302 - REDIRECT TO MyFood/
        assert view.status_code == 302
        assert view.url == "/myfood"

        request.GET = {
            "query": "3330720662002,4028491400907",
            "matching": "pate-a-tartiner"
        }
        view = save(request)
        assert view.status_code == 302
        assert view.url == "/myfood"

    def test_del_sub(self):
        request = RequestFactory().get("/del_sub")
        request.GET = {"query": "3330720662002,4028491400907"}
        request.user = User.objects.get(username="dev-purbeurre")
        view = del_sub(request)

        assert view.status_code == 302
        assert view.url == "/myfood"

    def test_my_food(self):
        request = RequestFactory().get("/del_sub")
        request.user = User.objects.get(username="dev-purbeurre")

        view = myfood(request)
        assert view.status_code == 200
