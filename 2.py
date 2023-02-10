# -*- coding: cp1251 -*-


def cylinder():
    print("Введите высоту")
    h = int(input())
    print("Введите радиус")
    r = int(input())
    S = 2 * 3.141592654 * r * h

    if input("Вы хотите получить площадь всего цилидра?\n").lower().strip() == "да":
        S += 2 * circle(r)
    return S


def circle(r):
    return 3.141592654 * r * r


if __name__ == "__main__":
    print(cylinder())