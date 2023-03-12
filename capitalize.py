
"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
Input Format
A single line of input containing the full name, S.
Output Format
Print the capitalized string, S.
Constraints
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
Sample Input
chris alan
Sample Output
Chris Alan
Sample Input
1 w 2 r 3g
Sample Output
1 W 2 R 3g
"""


def solve(s):
    s = s.lower()
    s = s.split()
    result = ""
    for item in s:
        temp = list(item)
        temp[0] = temp[0].upper()
        temp = "".join(temp)
        result += temp + " "

    return result[:-1]


def solve2(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s


if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)
    result = solve2(s)

    print(result)