n = int(input())
l = list(map(int, input().split()))

dp = [0 for i in range(n+1)]
last = -1
for i in range(n):
    if l[i] >= last:
        dp[i+1] = dp[i] + 1
    else:
        dp[i+1] = 1
    last = l[i]
print(max(dp))