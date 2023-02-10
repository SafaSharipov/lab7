# -*- coding: cp1251 -*-


def repeat():
    n = int(input())
    res = 1
    while n != 0:
        res *= n
        n = int(input())
    return res


if __name__ == "__main__":
    print(repeat())