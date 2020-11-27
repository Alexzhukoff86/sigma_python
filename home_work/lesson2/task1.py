def task1():
    return [i for i in range(1000, 1501) if i % 3 == 0 and i % 8 == 0]


if __name__ == '__main__':
    print(task1())
