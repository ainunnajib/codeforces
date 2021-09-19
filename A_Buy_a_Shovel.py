k, r = map(int, input().split())
ans = 1
while (k*ans)%10 not in [0, r] and ans < 10:
    ans += 1
print(ans)