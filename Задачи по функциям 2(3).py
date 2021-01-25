from random import randint
q1 = int(input('Диапазон минимума'))
q2 = int(input('Диапазон максимума'))
if q1<q2:
    c = []
    n = 10
    for i in range(1, n + 1):
        a = [randint(q1, q2)]
        c += a
    print(c)
else:
    print("а вот так нельзя:)")