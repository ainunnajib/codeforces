n = int(input())
l = list(map(int, input().split()))
c = 0
u = 0
for x in l:
    if x == -1:
        if c > 0:
            c -= 1
        else:
            u += 1
    else:
        c += x
print(u)