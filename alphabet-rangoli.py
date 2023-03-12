alpha = list('abcdefghijklmnopqrstuvwxyz')


def print_rangoli(size):
    for row in range((2 * size - 1) // 2 + 1):
        length = 4 * size - 3
        for col in range(length // 2 - 2 * row):
            print('-', end='')

        alpha_index = 2 * row + 1
        col = alpha_index
        while col > 0:
            print(alpha[col], end='')

            col -= 1

            if col not in [0, length - 1]:
                print('-', end='')

        for col in range(length // 2 - 2 * row):
            print('-', end='')

        print()

    for row in range((2 * size - 1) // 2 + 1):
        length = 4 * size - 3
        for col in range(length // 2 - 2 * row):
            print('-', end='')

        alpha_index = 2 * row + 1
        col = alpha_index
        while col > 0:
            print(alpha[col], end='')

            col -= 1

            if col not in [0, length - 1]:
                print('-', end='')

        for col in range(length // 2 - (2 * row)):
            print('-', end='')

        print()



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
