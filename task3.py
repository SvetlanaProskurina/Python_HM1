#Напишите программу, которая принимает на вход координаты точки (X и Y),
# #  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 ->3


XY = input('введите координаты точки через запятую \n')
s = ".:;!_*+()/#%&"
for char in s:
    if char in XY:#or XY.isdigit()!=True:
        print('введите верно, через запятую')
    else:
        in_XY = XY.split(",")


def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


if isint(in_XY[0]) and isint(in_XY[1]):
    X_=int(in_XY[0])
    Y_=int(in_XY[1])
    print(X_, Y_)
    if X_ > 0 and Y_ > 0:
        print('x = ', X_, 'y = ', Y_, '-> 1')
    if X_ < 0 and Y_ > 0:
        print('x = ', X_, 'y = ', Y_, '-> 2')
    if X_ < 0 and Y_ < 0:
        print('x = ', X_, 'y = ', Y_, '-> 2')
    if X_ > 0 and Y_ < 0:
        print('x = ', X_, 'y = ', Y_, '-> 4')
else:
    print('введены буквы, введите верно, ЧИСЛА через запятую')