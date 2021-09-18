t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ok = True
    for i in range(n-1):
        if l[i+1]-l[i] > 1:
            ok = False
            break
    print('YES' if ok else 'NO')