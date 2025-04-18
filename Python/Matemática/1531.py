# Fibonacci - Time Limit Exceeded

def pisano_period(m):
    a, b = 0, 1
    for i in range(m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1

def fibonacci_mod(n, m):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1 % m
    def mat_mult(a, b):
        return [
            [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % m, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % m],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % m, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % m]
        ]
    def mat_pow(mat, power):
        result = [[1, 0], [0, 1]]
        while power:
            if power % 2 == 1:
                result = mat_mult(result, mat)
            mat = mat_mult(mat, mat)
            power //= 2
        return result

    mat = [[1, 1], [1, 0]]
    res = mat_pow(mat, n-1)
    return res[0][0] % m

while True:
    try:
        n, m = map(int, input().split())
        pisano = pisano_period(m)
        idx = fibonacci_mod(n, pisano)
        result = fibonacci_mod(idx, m)
        print(result)
    except EOFError:
        break