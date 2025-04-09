# Triângulo

A, B, C = map(float, input().split())

if A + B > C and A + C > B and B + C > A:
    print("Perimetro = %.1f" % (A + B + C))
else:
    print("Area = %.1f" % ((A + B) * C / 2))