from home_work.lesson5.task2 import HAWAIIAN, MARGHERITA, PEPPERONI


class Pizza:
    count = 0

    def __init__(self, ingredients=None):
        Pizza.count += 1
        self._order_number = Pizza.count
        self._ingredients = ingredients

    @property
    def order_number(self):
        return self._order_number

    @property
    def ingredients(self):
        return self._ingredients

    @classmethod
    def pepperoni(cls):
        return Pizza(PEPPERONI)

    @classmethod
    def hawaiian(cls):
        return Pizza(HAWAIIAN)

    @classmethod
    def margherita(cls):
        return Pizza(MARGHERITA)
