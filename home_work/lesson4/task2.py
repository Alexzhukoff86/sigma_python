import pytest


def replace_first_char(input_string: str) -> str:
    """
    Function replaces first char in input_string to '_'
    :param input_string:
    :return:
    str
    """
    new_string = input_string.replace(input_string[0],'_')
    return "".join([input_string[0], new_string[1:]])


@pytest.mark.parametrize('test_data, expected', [('abracadabra', 'abr_c_d_br_'),
                                                 ('cocainum','co_ainum'),
                                                 ('ccccccc','c______')])
def test_function(test_data, expected):
    assert replace_first_char(test_data) == expected, f"Wrong Actual result"
