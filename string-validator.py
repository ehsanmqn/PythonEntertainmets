import re


def hasAlphaNumeric(s):
    match = re.findall('[a-zA-Z0-9]+', s)
    return len(match) > 0

def hasAlpha(s):
    match = re.findall('[a-zA-Z]+', s)
    return len(match) > 0


def hasDigit(s):
    match = re.findall('[0-9]+', s)
    return len(match) > 0


def hasUpper(s):
    match = re.findall('[A-Z]+', s)
    return len(match) > 0


def hasLower(s):
    match = re.findall('[a-z]+', s)
    return len(match) > 0


if __name__ == '__main__':
    # s = input()
    s = 'qA2'
    print(hasAlphaNumeric(s))
    print(hasAlpha(s))
    print(hasDigit(s))
    print(hasLower(s))
    print(hasUpper(s))
