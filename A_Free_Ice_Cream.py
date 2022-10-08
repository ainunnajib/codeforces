n, x = map(int, input().split())
d = 0
for _ in range(n):
    o, v = input().split()
    v = int(v)
    if o == '+':
        x += v
    else:
        if x >= v:
            x -= v
        else:
            d += 1
print(x, d)