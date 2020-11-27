def task5(cards):
    COSTS_PLUS_ONE = ['2', '3', '4', '5', '6']
    COSTS_ZERO = ['7', '8', '9']
    COSTS_MINUS_ONE = ['10', "'J'", "'Q'", "'K'", "'A'"]
    final_sum = 0
    for i in cards:
        if i in COSTS_PLUS_ONE:
            final_sum += 1
        elif i in COSTS_MINUS_ONE:
            final_sum -= 1
        elif i in COSTS_ZERO:
            final_sum += 0
        else:
            print(f'Wrong card {i}')
    return final_sum


if __name__ == '__main__':
    input_cards = input().split(', ')
    print(f'total cost = {task5(input_cards)}')
