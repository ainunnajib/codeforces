n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
x = 5 - k
ans = 0
for c in l:
    if c > x:
        break
    ans += 1
print(ans//3)