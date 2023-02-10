# -*- coding: cp1251 -*-


def get_input():
    return input()


def test_input(n):
    return str(n).isdigit()


def string_to_int(n):
    return int(n)


def print_int(n):
    print(n)

if __name__ == "__main__":
    n = get_input()
    if test_input(n):
        print_int(string_to_int(n))