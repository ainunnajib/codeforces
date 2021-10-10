from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    s = sum(l)
    x = [l[i]*n for i in range(n)]
    d = defaultdict(int)
    for i in x:
        d[i] += 1
    count = 0
    for i in d:
        if i == s:
            count += d[i]*(d[i]-1)
        elif 2*s-i in d:
            count += d[i]*d[2*s-i]
    print(count//2)