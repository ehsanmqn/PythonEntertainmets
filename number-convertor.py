def print_formatted(input_num):
    for number in range(1, input_num + 1):
        padding = len(str(bin(input_num))[2:])

        binary = bin(number)
        binary_str = str(binary)[2:]
        octal_str = str(oct(number))[2:]
        hexadecimal_str = (str(hex(number))[2:]).upper()

        decimal = "".join([' '] * (padding - len(str(number)))) + str(number)
        octal = "".join([' '] * (padding - len(str(octal_str)))) + str(octal_str)
        hexadecimal = "".join([' '] * (padding - len(str(hexadecimal_str)))) + str(hexadecimal_str)
        binary = "".join([' '] * (padding - len(str(binary_str)))) + str(binary_str)

        print("{} {} {} {}".format(decimal, octal, hexadecimal, binary))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
