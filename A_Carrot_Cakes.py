n, t, k, d = map(int, input().split())

t1 = ((n+k-1)//k) * t

t2 = max(0, t1 - d)
if t2 > t:
    print("YES")
else:
    print("NO")