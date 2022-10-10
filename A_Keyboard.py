a = 'qwertyuiopasdfghjkl;zxcvbnm,./'
c = input()
ans = ''
if c == 'R':
    for x in input():
        ans += a[a.index(x)-1]
else:
    for x in input():
        ans += a[a.index(x)+1]
print(ans)