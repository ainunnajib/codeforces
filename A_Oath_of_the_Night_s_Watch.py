n = int(input())
l = list(map(int, input().split()))
l.sort()
m = l[0]
i = 0
while i < n and l[i] == m:
    i += 1
if i == n:
    print(0)
else:
    j = n-1
    m = l[-1]
    while j >= 0 and l[j] == m:
        j -= 1
    print(j-i+1)