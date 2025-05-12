# Intervalo 2

N = int(input())
in_count = 0
out_count = 0

for _ in range(N):
    x = int(input())
    if 10 <= x <= 20:
        in_count += 1
    else:
        out_count += 1

print(f"{in_count} in")
print(f"{out_count} out")