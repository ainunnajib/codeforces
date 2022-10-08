n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    x -=1
    y -=1
    if x > 0:
        a[x-1] += max(0, y)
    if x < n-1:
        a[x+1] += max(0, a[x]-y-1)
    a[x] = 0

for v in a:
    print(v)