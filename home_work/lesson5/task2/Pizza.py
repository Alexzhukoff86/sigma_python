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
        """
        Create PEPPERONI with predefined ingredients
        :return:
        """
        return Pizza(PEPPERONI)

    @classmethod
    def hawaiian(cls):
        """
        Create HAWAIIAN with predefined ingredients
        :return:
        """
        return Pizza(HAWAIIAN)

    @classmethod
    def margherita(cls):
        """
        Create MARGHERITA with predefined ingredients
        :return:
        """
        return Pizza(MARGHERITA)
