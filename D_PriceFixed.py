n = int(input())
l = []
needed = 0
for _ in range(n):
    a, b = map(int, input().split())
    needed += a
    l.append(([b, a]))
l.sort()
items, total = 0, 0
i, j = 0, n-1
while(items < needed):
    if l[i][0] <= items:
        buy = l[i][1]
        l[i][1] = 0
        items += buy
        total += buy
        i += 1
    else:
        if l[j][1] >= l[i][0] - items:
            buy = l[i][0] - items
            l[j][1] -= buy
            items += buy
            total += buy*2
            if l[j][1] == 0:
                j -= 1
        else:
            buy = l[j][1]
            l[j][1] = 0
            items += buy
            total += buy*2
            j -= 1
print(total)