a = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
x = 0
for c in input():
    y = (a.index(c) - x)%26
    ans += min(y, 26-y)
    x = a.index(c)
print(ans)