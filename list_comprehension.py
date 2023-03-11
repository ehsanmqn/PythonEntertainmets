"""
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

Ref: https://www.w3schools.com/python/python_lists_comprehension.asp
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x_list = [a for a in range(0, x + 1)]
    y_list = [a for a in range(0, y + 1)]
    z_list = [a for a in range(0, z + 1)]

    result = [[i, j, k] for i in x_list
                        for j in y_list
                        for k in z_list if (i + j + k) != n]
    print(result)