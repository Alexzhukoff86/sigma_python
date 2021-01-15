from functools import wraps


def decorator_count(outer_func):
    @wraps(outer_func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return outer_func(*args, **kwargs)

    wrapper.count = 0

    return wrapper
