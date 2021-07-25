"""
TEST BUILDER, API REQUESTS & WRAPPER
"""
from webapp.modules.tools.builder import build_response
from webapp.modules.tools.tests.mocks import (
    MOCK_PROD_RESP,
    MOCK_FULL_PROD_RESP,
    MOCK_NAME,
    MOCK_CATEGORY,
    MOCK_PROD_FOR_DB,
    MOCK_FULL_PROD_FOR_DB,
)


# FROM API
def test_if_build_response_by_code_return_expected_data_api():

    assert build_response("3017620422003", "code", 0) == MOCK_PROD_RESP
    assert build_response("3017620422003", "code", 1) == MOCK_FULL_PROD_RESP


# FROM DB
def test_if_build_response_by_code_return_expected_data_db():

    assert build_response("3502110009449", "code", 0) == MOCK_PROD_FOR_DB
    assert build_response("3502110009449", "code", 1) == MOCK_FULL_PROD_FOR_DB


def test_if_build_response_by_category_return_expected_data():

    assert build_response("Pates a tartiner", "category", "e") == MOCK_CATEGORY
    assert len(build_response("Pates a tartiner", "category")) == 6


def test_if_build_response_by_sub_category_return_expected_data():

    url = 'http://world.openfoodfacts.org/product/3017620422003'
    expected_resp = "pates-a-tartiner-au-cacao-et-aux-noisettes"
    assert build_response(url, "sub_category") == expected_resp


def test_if_build_response_by_name_return_expected_data():

    assert build_response("Nutella", "name") == MOCK_NAME
    assert len(build_response("Nutella", "name")) == 6
