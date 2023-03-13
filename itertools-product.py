from itertools import product


def cartesian_product(list1, list2):
    A = [list1, list2]
    return tuple(product(*A))


if __name__ == '__main__':
    list1 = list(input().split())
    list1 = [int(item) for item in list1]
    list2 = list(input().split())
    list2 = [int(item) for item in list2]

    result = cartesian_product(list1, list2)

    for item in result:
        print(item, end=' ')
