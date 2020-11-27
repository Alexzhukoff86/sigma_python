def task3(value):
    for i in range(0, value + 1):
        output = ''
        for j in range(0, i):
            output += '*'
        print(output)


if __name__ == '__main__':
    input_data = int(input())
    task3(input_data)
