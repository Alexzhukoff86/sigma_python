class Calculator:

    def add(self, a, b):
        """
        Fucntion return sum of two args
        :param a:
        :param b:
        :return:

        """
        try:
            result = a + b
        except Exception as error:
            result = "Invalid args type"
        return result

    def substract(self, a, b):
        """
        Function returns difference of two args
        :param a:
        :param b:
        :return:
        """
        try:
            result = a - b
        except Exception as error:
            result = "Invalid args type"
        return result

    def multiply(self, a, b):
        """
        Fucntion returns composition of two args
        :param a:
        :param b:
        :return:
        """
        if type(a) in (int, float) and type(b) in (int, float):
            result = a * b
        else:
            result = "Invalid args type"
        return result

    def divide(self, a, b):
        """Function returns quotient of two args"""
        if type(a) in (int, float) and type(b) in (int, float):
            try:
                result = a / b
            except ZeroDivisionError as error:
                result = "Divided by zero"
        else:
            result = "Invalid args type"
        return result

    def exponent(self, a, b):
        """
        Function returns exponent
        :param a:
        :param b:
        :return:
        """
        if type(a) in (int, float) and type(b) in (int, float):
            result = a**b
        else:
            result = "Invalid args type"
        return result
