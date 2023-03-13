"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

 has at least  distinct characters
Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


def find_sorted_occurrence(input_list):
    counter_list = dict()

    for item in input_list:
        counter_list[item] = input_list.count(item)

    return counter_list


if __name__ == '__main__':
    s = input()

    result = find_sorted_occurrence(sorted(list(s)))
    result = sorted(result.items(), key=lambda x:x[1], reverse=True)

    for counter in range(3):
        print("{} {}".format(result[counter][0], result[counter][1]))
