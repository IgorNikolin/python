from random import randint
b = []
c = []
n = 15
for i in range(0,n):
    a = [randint(-100, 100)]
    print(a)
    if a[0] < 0:
        c += a
        c.sort(reverse = True)
    else:
        b += a
        b.sort()
print("Отрицательный массив", c)
print("Положительный массив", b)