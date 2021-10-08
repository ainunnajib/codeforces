t = list(input())
n = len(t)
p = input()
l = list(map(int, input().split()))
for i in range(n):
    l[i] -= 1

def check(m):
    s = t.copy()
    for i in range(m):
        s[l[i]] = ' '
    j = 0
    for c in p:
        while j<n and s[j] != c:
            j += 1
        if j==n:
            return False
        j += 1
    return True

lo = 0
hi = n+1
while(lo<hi-1):
    mid = lo + (hi-lo)//2
    if(check(mid)):
        lo = mid
    else:
        hi = mid
print(lo)