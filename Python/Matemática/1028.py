# Figurinhas

import math

NumerosDeCasosdeTeste = int(input())
for i in range(NumerosDeCasosdeTeste):
    F1, F2 = map(int, input().split())
    print(math.gcd(F1, F2))