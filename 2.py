# -*- coding: cp1251 -*-


def cylinder():
    print("������� ������")
    h = int(input())
    print("������� ������")
    r = int(input())
    S = 2 * 3.141592654 * r * h

    if input("�� ������ �������� ������� ����� �������?\n").lower().strip() == "��":
        S += 2 * circle(r)
    return S


def circle(r):
    return 3.141592654 * r * r


if __name__ == "__main__":
    print(cylinder())