t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    m = l[0]+l[1]
    x = 2 * (h // m)
    h %= m
    if h > l[0]:
        x += 2
    elif h > 0:
        x += 1
    print(x)
