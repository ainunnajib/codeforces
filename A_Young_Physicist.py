n = int(input())
x, y, z = 0, 0, 0
for _ in range(n):
    a, b, c = map(int, input().split())
    x += a
    y += b
    z += c
print('YES' if x == 0 and y == 0 and z == 0 else 'NO')