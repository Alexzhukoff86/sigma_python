def task2(temperature):
    unit = temperature[-1]
    value = int(temperature[0:-1])
    if unit == 'C':
        result = int((value * 9/5) + 32)
        return f'{temperature} is {result}F'
    elif unit == 'F':
        result = int((value - 32) * 5/9)
        return f'{temperature} is {result}C'
    else:
        return 'Wrong unit'


if __name__ == '__main__':
    input_data = input()
    print(task2(input_data))
