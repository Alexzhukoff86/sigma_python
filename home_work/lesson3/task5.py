from functools import reduce
from typing import List


def get_sum_of_elements(input_list: List) -> int:
    """

    :param input_list:
    :return:
    """
    result_sum = 0
    for i in input_list:
        if isinstance(i, list):
            result_sum += get_sum_of_elements(i)
        else:
            result_sum += i
    return result_sum


if __name__ == '__main__':
    test = [1, 2, [3, 4], [5, 6, [7, 8, 9, 10]]]
    print(get_sum_of_elements(test))
