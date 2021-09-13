n = int(input())
ans = 0
for _ in range(n):
    x = sum(map(int, input().split()))
    if x >= 2:
        ans += 1
print(ans)