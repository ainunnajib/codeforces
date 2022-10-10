n = int(input())
l = list(map(int, input().split()))
s = sorted(l, reverse=True)
d = set()
i = 0
for x in l:
    d.add(x)
    while s[i] in d:
        print(s[i], end=' ')
        i += 1
        if i == n:
            break
    print()