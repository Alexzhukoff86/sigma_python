from typing import List

import pytest


def get_isalnum_words(input_sentence: str) -> List:
    """
    Function returns all isalnum words from input sentence
    :param input_sentence:
    :return:
    list
    """
    return [x for x in input_sentence.split() if x.isalnum() and not x.isalpha() and not x.isnumeric()]


@pytest.mark.parametrize('test_data, expected',
                         [('Dash100 apps are rendered in the web3 browser55', ['Dash100', 'web3', 'browser55']),
                          ('My name is test123!', [])])
def test_function(test_data, expected):
    assert get_isalnum_words(test_data) == expected, "Actual list are wrong"
