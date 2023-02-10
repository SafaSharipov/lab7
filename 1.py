# -*- coding: cp1251 -*-


def test():
    n = int(input())
    if n >= 0:
        positive()
    else:
        negative()


def positive():
    print("Положительное")


def negative():
    print("Негативное")

if __name__ == "__main__":
    test()