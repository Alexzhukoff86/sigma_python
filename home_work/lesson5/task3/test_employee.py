import pytest

from home_work.lesson5.task3.Employee import Employee


@pytest.mark.parametrize("first_name, expected", [("JOAN", "Joan"), ("tom", "Tom")])
def test_first_name_property(first_name, expected):
    employee = Employee(first_name, 'Smith', 85000)
    assert employee.first_name == expected

@pytest.mark.parametrize("last_name, expected", [("JOAN", "Joan"), ("tom", "Tom")])
def test_last_name_property(last_name, expected):
    employee = Employee("Alex", last_name, 8500)
    assert employee.last_name == expected

def test_fullname_property():
    employee = Employee('JOAN', 'Smith', 85000)
    assert employee.fullname == 'Joan Smith'


def test_salary_property():
    employee = Employee('JOAN', 'Smith', 85000)
    assert employee.salary == 85000


def test_employee_from_string():
    employee = Employee.from_string('John-doe-73000')
    assert employee.first_name == 'John'
    assert employee.fullname == 'John Doe'
    assert employee.salary == 73000
