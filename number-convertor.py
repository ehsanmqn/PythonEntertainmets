def print_formatted(input_num):
    for number in range(1, input_num + 1):
        binary = bin(number)
        decimal = "".join([' '] * (len(str(binary)) - len(str(number)))) + str(number)
        octal = "".join([' '] * (len(str(binary)) - len(str(oct(number))))) + str(oct(number))
        hexadecimal = "".join([' '] * (len(str(binary)) - len(str(hex(number))))) + str(hex(number))
        binary = "".join([' '] * (len(str(binary)) - len(str(bin(number))))) + str(bin(number))

        print("{}{}{}{}".format(decimal, octal, hexadecimal, binary))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)