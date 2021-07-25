"""
TEST CLEANER
IN PROGRESS
"""

from webapp.modules.tools.clean_sentence import (
    remove_special_char, clean_query, clean_accents, clean_space
)


def test_if_remove_special_char_return_expected_data():

    mock = remove_special_char("a[b\"c/\\d:e?f!g-h}i>j<k(l)m{n,o]p&", "all")
    assert mock == "abcdefghijklmnop"

    # ADD SPACE FOR ==> " or - or ,
    mock = remove_special_char("I\"m testing-remove special char,thanks",
                               "add_space")
    assert mock == "i m testing remove special char thanks"


def test_if_clean_query_return_none():

    assert clean_query("") is None
    assert clean_query(" ") is None


def test_if_clean_query_return_int():

    assert clean_query("123") == 123


def test_if_clean_query_return_expected_data():

    assert clean_query("pain<,au-lait") == "pain au lait"


def test_if_clean_accents_return_expected_data():

    assert clean_accents("àâäéèêëîïôöùûü") == "aaaeeeeiioouuu"


def test_if_clean_space_return_expected_data():

    assert clean_space(" remove space", "-") == "remove-space"
