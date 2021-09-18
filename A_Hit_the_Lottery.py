n = int(input())
ans = 0
for i in [100, 20, 10, 5, 1]:
    ans += n//i
    n %= i
print(ans)