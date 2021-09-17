n, h = map(int, input().split())
ans = 0
for x in list(map(int, input().split())):
    if x > h:
        ans += 2
    else: ans += 1
print(ans)