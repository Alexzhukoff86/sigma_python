import pytest

from home_work.lesson5.task1.Calculator import Calculator


@pytest.fixture()
def calculator():
    calc = Calculator()
    yield calc


@pytest.mark.parametrize("first_arg, second_arg, expected", [(10, 5, 15), (0, 0, 0), (-1, 1, 0)])
def test_calculator_add(first_arg, second_arg, expected, calculator):
    assert calculator.add(first_arg, second_arg) == expected


@pytest.mark.parametrize("first_arg, second_arg, expected",
                         [("a", 0, "Invalid args type"), (3, None, "Invalid args type")])
def test_calculator_add_exception(first_arg, second_arg, expected, calculator):
    assert calculator.add(first_arg, second_arg) == expected


@pytest.mark.parametrize("first_arg, second_arg, expected", [(10, 5, 5), (-1, -1, 0), (4, 6, -2)])
def test_calculator_subtract(first_arg, second_arg, expected, calculator):
    assert calculator.substract(first_arg, second_arg) == expected


@pytest.mark.parametrize("first_arg, second_arg, expected",
                         [("a", 0, "Invalid args type"), (3, None, "Invalid args type")])
def test_calculator_subtract_exception(first_arg, second_arg, expected, calculator):
    assert calculator.substract(first_arg, second_arg) == expected


@pytest.mark.parametrize("first_arg, second_arg, expected", [(10, 5, 50), (100, 0, 0), (1, 1, 1)])
def test_calculator_multiply(first_arg, second_arg, expected, calculator):
    assert calculator.multiply(first_arg, second_arg) == expected


@pytest.mark.parametrize("first_arg, second_arg, expected",
                         [("a", 0, "Invalid args type"), (3, None, "Invalid args type")])
def test_calculator_multiply_exception(first_arg, second_arg, expected, calculator):
    assert calculator.multiply(first_arg, second_arg) == expected, f"Wrong calculation for {first_arg} and {second_arg}"


@pytest.mark.parametrize("first_arg, second_arg, expected", [(10, 5, 2), (100, 1, 100), (0, 1, 0)])
def test_calculator_divide(first_arg, second_arg, expected, calculator):
    assert calculator.divide(first_arg, second_arg) == expected


@pytest.mark.parametrize("first_arg, second_arg, expected",
                         [("a", 0, "Invalid args type"), (3, None, "Invalid args type"), (3, 0, "Divided by zero")])
def test_calculator_divide_exception(first_arg, second_arg, expected, calculator):
    assert calculator.divide(first_arg, second_arg) == expected, f"Wrong calculation for {first_arg} and {second_arg}"


@pytest.mark.parametrize("first_arg, second_arg, expected", [(3, 2, 9), (10, 10, 10000000000), (10, 1, 10), (3, 0, 1)])
def test_calculator_exponent(first_arg, second_arg, expected, calculator):
    assert calculator.exponent(first_arg, second_arg) == expected


@pytest.mark.parametrize("first_arg, second_arg, expected",
                         [("a", 0, "Invalid args type"), (3, None, "Invalid args type")])
def test_calculator_exponent_exception(first_arg, second_arg, expected, calculator):
    assert calculator.exponent(first_arg, second_arg) == expected, f"Wrong calculation for {first_arg} and {second_arg}"
