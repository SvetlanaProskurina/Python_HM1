#Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

import math


XY1 = input('введите координаты первой точки через запятую \n')
XY2 = input('введите координаты второй точки через запятую \n')

def SplitStr(str):
    s = ".:;!_*+()/#%&"
    for char in s:
        if char in str:
            return False
        else:
            str_out = str.split(",")
            return str_out


def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


if isint(SplitStr(XY1)[0]) and isint(SplitStr(XY1)[1]) and isint(SplitStr(XY2)[0]) and isint(SplitStr(XY2)[1]):

    X1 = int(SplitStr(XY1)[0])
    Y1 = int(SplitStr(XY1)[1])
    X2 = int(SplitStr(XY2)[0])
    Y2 = int(SplitStr(XY2)[1])
    print('длина отрезка между точками (', X1,',',Y1,') и (', X2,',',Y2,') равна ', str(round(math.sqrt((X2-X1)**2 + (Y2-Y1)**2),3))[:-1]) # форматирует строку , округляя до 3х знаков и убирает последний символ

else:
    print('введите верно значения координат')