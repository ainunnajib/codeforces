from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    l = defaultdict(int)
    r = defaultdict(int)
    ll = defaultdict(list)
    lr = defaultdict(list)
    for i in range(n):
        x, y = map(int, input().split())
        l[x] += 1
        r[y] += 1
        ll[x].append(y)
        lr[y].append(x)
    sl = defaultdict(int)
    for x in ll:
        for y in ll[x]:
            sl[x] += r[y]
    
    invalid = 0
    for x in l:
        invalid += (l[x]-1) * (sl[x] - l[x])
    
    print(n*(n-1)*(n-2)//6 - invalid)
