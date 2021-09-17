n = int(input())
ans = 0
c = ''
for _ in range(n):
    x = input()[0]
    if x != c:
        ans += 1
        c = x
print(ans)