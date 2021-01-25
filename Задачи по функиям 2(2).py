from random import randint
c = []
n=10
for i in range(1,n+1):
    a = [randint(1, 10)]
    c += a
    print(a)
print(sum(c))