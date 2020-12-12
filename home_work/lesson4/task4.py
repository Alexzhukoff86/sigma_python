import os
from typing import List


def write_bytearray_to_file(filepath, input_string: str) -> List:
    """
    Writes to filepath bytearray of chars from input_string
    :param filepath:
    :param input_string:
    :return:
    """
    result = bytearray()
    filename = os.path.join(filepath, 'file.bin')
    with open(filename, 'wb') as file:
        byte_array = bytearray()
        byte_array.extend(map(ord, input_string))
        file.write(byte_array)

    with open(filename, 'rb') as file:
        filebytes = file.read()
        for byte in filebytes:
            result.append(byte)
    return list(result)


def test_function():
    test_file = '/home/alexzhukoff86/Projects'
    test_string = 'Hello Python'
    expected_result = [72, 101, 108, 108, 111, 32, 80, 121, 116, 104, 111, 110]
    assert write_bytearray_to_file(test_file, test_string) == expected_result, "Just a message"
