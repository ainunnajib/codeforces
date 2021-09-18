n = int(input())
l = list(map(int, input().split()))
best, worst = l[0], l[0]
amazing = 0
for x in l[1:]:
    if x > best:
        amazing += 1
        best = x
    if x < worst:
        amazing += 1
        worst = x
print(amazing)