
def door_mat(n, m):
    for row in range(n // 2):
        cols = (m - 3 * (2 * row + 1)) // 2
        for col in range(cols):
            print('-', end='')
        for col in range(2 * row + 1):
            print('.|.', end='')
        for col in range(cols):
            print('-', end='')
        print()

    for col in range((m - 7) // 2):
        print('-', end='')

    print('WELCOME', end='')

    for col in range((m - 7) // 2):
        print('-', end='')

    print()
    for row in range(n // 2, 0, -1):
        cols = (m - 3 * (2 * row - 1)) // 2
        for col in range(cols):
            print('-', end='')
        for col in range(2 * row - 1):
            print('.|.', end='')
        for col in range(cols):
            print('-', end='')
        print()
    print()


if __name__ == '__main__':
    line = input()
    line = line.split()
    N = int(line[0])
    M = int(line[1])
    door_mat(N, M)
