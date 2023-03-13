"""
Problem:-
Implement a function that takes a string that consists of lowercase letters and digits and returns a string that consists of all digits and lowercase English letters that are not present in the string. The digits should come first, in ascending order, followed by characters, also in ascending order.

Example
S = "7985interdisciplinary 12"
The returned string is "0346bfghjkmoquwwa It contains all missing digits in ascending order, followed by missing characters in ascending order.

Function Description
Complete the function missingcharacters in the editor below.

missingCharacters has the following parameter(s):
    string s:  a string
Return:
    string: a string as described above
"""


def missingCharacters(input_string):
    input_string_len = [0] * 123
    output_string = ""
    for i in range(len(input_string)):
        x = ord(input_string[i])
        input_string_len[x] += 1

    for i in range(48, 58):
        if input_string_len[i] == 0:
            output_string += chr(i)

    for i in range(97, 123):
        if input_string_len[i] == 0:
            output_string += chr(i)

    return output_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
