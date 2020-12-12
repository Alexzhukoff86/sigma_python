import pytest


def get_first_and_last_chars(input_string: str) -> str:
    """
    Function returns new strings contains first 2 chars and last 2 chars from input string
    :param input_string:
    :return:
    str
    """
    if len(input_string) < 2:
        return ''
    return "".join([input_string[:2], input_string[-2:]])


@pytest.mark.parametrize("test_data, expected", [("Winter", "Wier"), ('r2', 'r2r2'), ('p', '')])
def test_function(test_data, expected):
    assert get_first_and_last_chars(test_data) == expected, f"Actual result are wrong"
