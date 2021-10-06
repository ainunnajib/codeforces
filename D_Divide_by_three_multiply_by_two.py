n = int(input())
l = list(map(int, input().split()))

f = []
for x in l:
    a, b, c = 0, 0, x
    while c%2 == 0:
        c //= 2
        a += 1
    while c%3 == 0:
        c //= 3
        b -= 1
    f.append((a, b, x))
f.sort()
s = [str(f[i][2]) for i in range(n)]
print(' '.join(s))