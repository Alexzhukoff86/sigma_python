import logging
import time
from datetime import datetime
from functools import wraps
import random


def decorator_execution_time(outer_function):
    @wraps(outer_function)
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename="execution_time.log", level=logging.INFO)

        start_time = time.time()
        result = outer_function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f" function: {outer_function.__name__} with {args} and {kwargs} takes {execution_time}")
        return result

    return wrapper


if __name__ == '__main__':
    @decorator_execution_time
    def _function(*args, **kwargs):
        sleep_time = random.randint(1,5)
        time.sleep(sleep_time)
    _function("string", type="func")