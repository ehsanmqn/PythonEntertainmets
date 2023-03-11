import math


def average(data):
    return sum(data) / len(data)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("{:.2f}".format(average(student_marks[query_name])))
