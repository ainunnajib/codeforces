n, k = map(int, input().split())
l = list(map(int, input().split()))
ps = [0 for i in range(n)]
ps[0] = l[0]
for i in range(1, n):
    ps[i] = ps[i-1] + l[i]
minx = 0
minsum = ps[k-1]
for i in range(n-k):
    if ps[i+k] - ps[i] < minsum:
        minsum = ps[i+k] - ps[i]
        minx = i+1
print(minx+1)