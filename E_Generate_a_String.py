n, x, y = map(int, input().split())

dp = [10**17 for i in range(n+1)]
# dp[n] = min(dp[n-1]+x, dp[n/2]+y dp[(n+1)/2]+x+y)
dp[0] = 0
dp[1] = x
for i in range(2, n+1):
    a = dp[i-1]+x
    b = 10**17
    if i%2 == 0:
        b = dp[i//2]+y
    else:
        b = dp[(i+1)//2]+x+y
    dp[i] = min(a, b)
print(dp[n])