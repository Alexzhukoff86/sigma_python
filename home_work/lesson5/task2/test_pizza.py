import pytest

from home_work.lesson5.task2.Pizza import Pizza


@pytest.fixture(scope="module")
def pizza():
    pizza = Pizza()
    yield pizza


def test_first_pizza_order(pizza):
    assert pizza.order_number == 1, "Wrong order_number"


def test_second_pizza_order(pizza):
    pizza1 = Pizza()
    assert pizza1.order_number == 2, "Wrong order_number"


def test_pizza_ingredients_as_argument():
    pizza = Pizza(['bacon', 'parmesan', 'ham'])
    assert pizza.ingredients == ['bacon', 'parmesan', 'ham'], "Wrong ingredients for custom pizza"


def test_create_pizza_pepperoni():
    pizza = Pizza.pepperoni()
    assert pizza.ingredients == ["bacon", "mozzarella", "oregano"], "Wrong ingredients for pepperoni pizza"


def test_create_pizza_hawaiian():
    pizza = Pizza.hawaiian()
    assert pizza.ingredients == ["ham", "pineapple"], "Wrong ingredients for hawaiian pizza"


def test_create_pizza_margherita():
    pizza = Pizza.margherita()
    assert pizza.ingredients == ["mozzarella", "olives", "tomatoes"], "Wrong ingredients for margherita pizza"
