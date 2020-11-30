from typing import List


def get_sorted_tuple(input_list1, input_list2) -> List:
    """
    Function zip two lists and return sorted list of tuples
    via second element in tuple
    :param input_list1:
    :param input_list2:
    :return:
    list of sorted tuples
    """
    unsorted_tuple = zip(input_list1, input_list2)
    sorted_tuple = sorted(unsorted_tuple, key=lambda x: x[1])
    return list(sorted_tuple)


if __name__ == '__main__':
    weekdays = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
    days = [7, 6, 5, 4, 3, 2, 1]
    print(get_sorted_tuple(weekdays, days))
