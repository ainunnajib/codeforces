n = int(input())
l = list(map(int, input().split()))
t = max(l)
s = min(l)
dt = l.index(t)
ds = l[::-1].index(s)
d = dt + ds
if d > n-2:
    d -= 1
print(d)