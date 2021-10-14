from collections import defaultdict
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    d = [n-l[i] for i in range(k)]
    d.sort()
    t = 0
    m = 0
    for i in range(k):
        if t + d[i] < n:
            t += d[i]
            m += 1
    print(m)