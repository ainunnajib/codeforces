t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    if n < 3:
        floor = 1
    else:
        n -= 2
        floor = 2
        while n > x:
            n -= x
            floor += 1
    print(floor)
