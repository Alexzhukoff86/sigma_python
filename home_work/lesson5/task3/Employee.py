from home_work.lesson5.task3.Human import Human


class Employee(Human):

    def __init__(self, first_name: str, last_name, salary):
        super().__init__(first_name, last_name)
        self._salary = int(salary)

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def fullname(self):
        return self._fullname

    @property
    def salary(self):
        return self._salary

    @classmethod
    def from_string(cls, employee_data):
        """
        Function create Employee from string
        :param employee_data:
        :return:
        """
        employee_data_list = employee_data.split('-')
        employee = Employee(*employee_data_list)
        return employee
