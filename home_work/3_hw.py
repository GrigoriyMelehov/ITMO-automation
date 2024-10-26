import random

def F_2(x =3, y=5):
    if  x > y:
        print(x)
    else:
        print(y)
    pass

def F_3(x=136, y=1):
    if abs(x - y) == 135:
        print('YES')
    else:
        print('NO')
    pass

def F_4(x=9):
    if x == 1 or x == 2 or x == 12:
        print('Зима')
    elif x in range(3, 5):
        print('Весна')
    elif 6 <= x <= 8:
        print('Лето')
    else:
        print('Осень')
    pass

def F_5(x=12, y= 15, z=22):
    if x > 10 and y > 10 and z > 10:
        print('yes')
    else:
        print('no')
    pass

def F_6(numbers: list=(1, 3, -5, 12, -7)):
    s = 0
    for i in range(0, 4):
        if numbers[i] > 0:
            s += 1
    print('в списке', s, 'положительных чисел')
    pass

def F_7(x: int=3, y: int=5):
    print(x*12*29+y*29, 'дней')
    pass


F_2()
F_3()
F_4()
F_5()
F_6()
F_7()