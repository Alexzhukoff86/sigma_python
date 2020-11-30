from typing import List


def get_palindromes(input_list: List) -> List:
    """
    Function returns list of palindromes
    :param input_list:
    :return list of str:
    """
    result_list = filter(lambda x: x if x == x[::-1] else None, input_list)
    return list(result_list)


if __name__ == '__main__':
    words = ["radar", "device", "level", "program", "kayak", "river", "racecar"]
    print(get_palindromes(words))
