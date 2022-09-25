#Напишите программу, которая по заданному номеру четверти, 
# показывает c (x и y).

quart = input('введите номер четверти \n')



def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

if isint(quart)==False: 
    print('Введите число от 1 до 4 включительно')
else:
    int_quart = int(quart)
    if int_quart==1:
        print('диапазон возможных координат точек (x,y) в ',int_quart,' четверти  x > 0 и y > 0')
    elif int_quart==2:
        print('диапазон возможных координат точек (x,y) в ',int_quart,' четверти  x < 0 и y > 0')
    elif int_quart==3:
        print('диапазон возможных координат точек (x,y) в ',int_quart,' четверти  x < 0 и y < 0')
    elif int_quart==4:
        print('диапазон возможных координат точек (x,y) в ',int_quart,' четверти  x > 0 и y > 0')
    else:
        print('Введите число от 1 до 4 включительно')