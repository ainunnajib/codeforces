n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
x = l[k-1]
i = 0
while i < n and l[i] >= x and l[i] > 0:
    i += 1
print(i)