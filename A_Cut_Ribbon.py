n, a, b, c = map(int, input().split())
dp = [0 for i in range(n+1)]
m = min(a,b,c)
dp[m] = 1
for i in range(m+1, n+1):
    if (i-a > 0 and dp[i-a] > 0) or i==a:
        dp[i] = max(dp[i-a]+1, dp[i])
    if (i-b > 0 and dp[i-b] > 0) or i==b:
        dp[i] = max(dp[i-b]+1, dp[i])
    if (i-c > 0 and dp[i-c] > 0) or i==c:
        dp[i] = max(dp[i-c]+1, dp[i])
print(dp[n])