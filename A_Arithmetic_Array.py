t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)
    if s == n:
        print(0)
    elif s < n:
        print(1)
    else:
        print(s-n)