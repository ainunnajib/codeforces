from collections import defaultdict
n = int(input())
l = list(map(int, input().split()))
d = defaultdict(int)
for i in l:
    d[i] += 1

dp = [0 for i in range(max(l)+1)]
dp[1] = d[1]
for i in range(2, max(l)+1):
    dp[i] = max(dp[i-1], dp[i-2] + d[i]*i)
print(dp[max(l)])