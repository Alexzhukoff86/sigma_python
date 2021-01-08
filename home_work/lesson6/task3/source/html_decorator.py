from functools import wraps


def html_decorator(html_tag, n):
    def inner_function(outer_function):
        @wraps(outer_function)
        def wrapper(text):
            result = list()
            result_text = outer_function(text)
            open_tag = f"<{html_tag}>"
            close_tag = f"</{html_tag}>"
            for i in range(1, n+1):
                result.append(f"{open_tag}{result_text} {i}{close_tag}")
            return result
        return wrapper
    return inner_function


@html_decorator('li', 3)
def html_element(text):
    spec_symbols = ['@', '#', '%', '&', '$', '^', '*', '_']
    remove_symbols = ['>', '<', '/']
    result_text = ''.join([' ' if x in spec_symbols else x for x in text])
    result_text = ''.join(['' if x in remove_symbols else x for x in result_text])
    return result_text.capitalize()
