t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ones = l.count(1)
    twos = l.count(2)
    gap = 2*twos - ones
    if gap > 0:
        gap %= 4
        if ones > 0:
            gap %= 2
    else:
        gap %= 2

    print('YES' if gap == 0 else 'NO')