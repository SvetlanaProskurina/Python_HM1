#Напишите программу, которая принимает на вход цифру, 
#обозначающую день недели, и проверяет, 
#является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

input_ = input('Введите цифру \n')

if isint(input_):
    InputNumber = int(input_)
    if InputNumber >= 1 and InputNumber <= 7:
        if InputNumber >= 1 and InputNumber <= 5:
            print('Этот день не является выходным')
        else:
            print('Этот день является выходным')
    else:
        print('введите число от 1 до 7')
else:
    print('введите числа')