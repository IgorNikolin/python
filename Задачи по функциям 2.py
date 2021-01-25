i = int(input("1) Круг 2)прямоугольник 3)треугольник"))
if i==1:
    A = int(input("введите значение Радиуса"))
    B = 3.14
    s = ((A*B)**2)
    print(round(s, 2));
elif i==2:
    A = int(input("Введите значение высоты"))
    B = int(input("Введите значение ширины"))
    s = (A*B)
    print(s)
elif i==3:
    A = int(input("Введите значение основания"))
    B = int(input("Введите значение высоты"))
    s=(A*B)/2
    print(s)
else:
    print("error999999999999")
