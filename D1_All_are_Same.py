def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n-1):
        d = l[i+1] - l[i]
        if ans == 0:
            ans = d
        else:
            ans = gcd(ans, d)
    if ans == 0:
        ans = -1
    print(ans)