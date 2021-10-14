t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    s = a+b+c
    x, y, z = max(b, c) - a + 1, max(c, a) - b + 1, max(a, b) - c + 1
    x, y, z = max(0, x), max(0, y), max(0, z)
    print(x, y, z)