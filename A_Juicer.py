n, b, d = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
cur = 0
for x in a:
    if x > b:
        continue
    cur += x
    if cur > d:
        ans += 1
        cur = 0
print(ans)