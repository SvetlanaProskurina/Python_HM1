#Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


r = range(8)

for i in r:
    XYZ = ''
    while  i > 0:
        XYZ = str(i % 2) + XYZ
        i = i // 2
    if len(XYZ) == 0:
        XYZ = '000 '
    elif len(XYZ) == 1:
        XYZ = '00' + XYZ
    elif len(XYZ) == 2:
        XYZ = '0' + XYZ
    elif len(XYZ) == 3:
        XYZ = XYZ

    X_ = bool(int(XYZ[0]))
    Y_ = bool(int(XYZ[1]))
    Z_ = bool(int(XYZ[2]))

    if not (X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_):
        print('при X =',X_, ' и Y =',Y_, ' и Z =',Z_, 'выражение not (X_ or Y_ or Z_) == (not X_ and not Y_ and not Z_) истинно')
