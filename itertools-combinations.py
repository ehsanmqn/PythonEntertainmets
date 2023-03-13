from itertools import combinations


def cartesian_combinations(list1, length):

    result = []
    for l in range(1, length + 1):
        result.append(sorted(list(combinations(list1, l))))

    return result


if __name__ == '__main__':
    input_data = list(input().split())
    input_string = list(input_data[0])
    length = int(input_data[1])

    result = cartesian_combinations(sorted(input_string), length)

    sorted_result = []
    for item1 in result:
        for item2 in sorted(item1):
            sorted_result.append("".join(sorted(item2)))

    for item in sorted_result:
        print(item)
