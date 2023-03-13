from itertools import permutations


def char_permutations(input_string, length):
    list_string = list(input_string)
    return sorted(permutations(list_string, length))


if __name__ == '__main__':
    input_data = list(input().split())
    input_string = input_data[0]
    length = int(input_data[1])

    result = char_permutations(input_string, length)

    for item in result:
        print("".join(item))
