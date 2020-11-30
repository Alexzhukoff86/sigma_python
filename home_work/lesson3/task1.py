if __name__ == '__main__':
    x = int(input("Please input x: "))
    y = int(input("Please input y: "))
    print((lambda a, b: a / b if b != 0 else None)(x, y))

