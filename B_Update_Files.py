t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = 1
    ans = 0
    n -= 1
    while x <= k and n > 0:
        ans += 1
        n -= x
        x *= 2
    ans += n//k
    if n%k != 0:
        ans += 1
    print(ans)