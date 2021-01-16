from home_work.lesson7.task4.source.circe_function_generator import circle_function_generator


def test_circle_function_generator():
    circle_generator = circle_function_generator([1,2,3,4], 2)
    for c in circle_generator:
        print(c)