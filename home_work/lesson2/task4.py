def task4():
    output_list = list()
    for i in range(0,7):
        if i == 0 or i == 6:
            output_list.append('*'*7)
        else:
            row_str = ' '*7
            output_list.append("".join((row_str[i:],'*', row_str[:i])))
    for i in range(0,7):
        print(output_list[i])


if __name__ == '__main__':
    task4()
