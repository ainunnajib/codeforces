t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = [0 for i in range(n-1)]
    for i in range(n-1):
        m[i] = 10**(a[i+1]-a[i]) - 1

    ans = 0
    for i in range(n-1):
        if k >= m[i]:
            ans += m[i] * (10**a[i])
            k -= m[i]
        else:
            ans += (k+1) * (10**a[i])
            k = -1
            break
    if k >= 0:
        ans += (k+1) * (10**a[n-1])
    print(ans)