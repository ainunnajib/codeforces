t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    valid = False
    for __ in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        tile = (a, b, c, d)
        if b == c:
            valid = True
    if m%2 == 1:
        valid = False

    if valid:
        print('YES')
    else:
        print('NO')
