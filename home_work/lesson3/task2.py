from typing import List


def get_six_length_words(string_list: List) -> List:
    """
    Function get list of strings and returns
    list of words with length equls 6
    :param string_list:
    :return:
    list of strings
    """
    result_filter = filter(lambda x: len(x) == 6, string_list)
    return list(result_filter)


if __name__ == '__main__':
    test_string_list = ["5test", "9testtest", "3te", "6testt", "", "10testtest"]
    print("Result: ")
    print(get_six_length_words(test_string_list))
