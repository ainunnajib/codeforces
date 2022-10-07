a = list(map(int, input().split()))
l = input()
ans = 0
for c in l:
    ans += a[int(c)-1]
print(ans)