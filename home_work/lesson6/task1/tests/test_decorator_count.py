from home_work.lesson6.task1.source.decorator_count import decorator_count


@decorator_count
def function_under_test():
    pass


def test_decorator_count_once_call():
    function_under_test()
    assert function_under_test.count == 1, "Wrong fucntion calls count"


def test_decorator_count_twice_call():
    function_under_test()
    assert function_under_test.count == 2, "Wrong function calls count"
