n = int(input())
l = []
for _ in range(n):
    h, a = map(int, input().split())
    l.append((h, a))
ans = 0
for i in range(n):
    for j in range(n):
        if i == j: continue
        if l[i][0] == l[j][1]: ans += 1
print(ans)