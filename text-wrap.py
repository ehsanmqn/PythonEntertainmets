import textwrap


def wrap(string, max_width):
    chunks = [string[i:i+max_width] for i in range(0, len(string), max_width)]

    result = ""
    for item in chunks:
        result += item + "\n"
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
