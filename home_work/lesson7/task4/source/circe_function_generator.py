def circle_function_generator(sequence, max_length):
    index = 0
    while max_length > 0:
        max_length -= 1
        yield sequence[index]
        if index >= len(sequence)-1:
            index = 0
        else:
            index += 1
