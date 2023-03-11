if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    data = tuple(integer_list)

    print(hash(data))