n = int(input())
ans = 0
cur = 0
for _ in range(n):
    a, b = map(int, input().split())
    cur = max(0, cur-a+b)
    ans = max(ans, cur)
print(ans)