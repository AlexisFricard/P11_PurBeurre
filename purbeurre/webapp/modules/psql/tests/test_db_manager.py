"""
TEST CONNECTION TO DATABASE
"""
from purbeurre import wsgi  # noqa

from webapp.modules.tools.tests.mocks import MOCK_FULL_PROD_RESP
from webapp.models import Product, Nutriment, Save
from webapp.modules.psql.db_manager import (
    add_data, save_research, del_research
)


def test_save_research():

    # VARS
    list = ['codeOfSubstitute', 'codeOfProduct', 'johndoe']

    # EXECUTE FUNCTION
    save_research(list)

    """ TEST - IF WAS ADDED"""
    assert Save.objects.get(user='johndoe')
    assert save_research(list) is None


def test_del_research():

    # VARS
    research = [
        'codeOfProduct',
        'codeOfSubstitute',
        'johndoe'
    ]

    # EXECUTE FUNCTION
    del_research(research)

    """ TEST - AN INEXISTING SUBSTITUTION """
    assert len(Save.objects.filter(user='johndoe')) == 0


def test_add_data():

    # VAR
    mock_resp = MOCK_FULL_PROD_RESP

    # EXECUTE FUNCTION
    add_data(mock_resp)

    """ TEST - IF IT WAS ADDED AND DELETE IT """
    assert Product.objects.get(code='3017620422003').delete()
    assert Nutriment.objects.get(code='3017620422003').delete()
