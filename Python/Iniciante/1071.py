# Soma de Impares Consecutivos I

x = int(input())
y = int(input())
if x > y:
    x, y = y, x
s = 0
for i in range(x + 1, y):
    if i % 2 != 0:
        s += i
print(s)