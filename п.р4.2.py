str = input().split()
result = 0


def sum(a, b):
    return a + b


def dif(a, b):
    return a - b


def pr(a, b):
    return a * b


def div(a, b):
    return a / b


a = int(str[0])
b = int(str[2])

while str != 'q':
    if str[1] == '+':
        result = sum(a, b)
        print(result)
    if str[1] == '-':
        result = dif(a, b)
        print(result)
    if str[1] == '*':
        result = pr(a, b)
        print(result)
    if str[1] == ':':
        result = div(a, b)
        print(result)
    str = input().split()
    a = int(str[0])
    b = int(str[2])



