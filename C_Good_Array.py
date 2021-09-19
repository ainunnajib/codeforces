from collections import defaultdict
c = defaultdict(int)

n = int(input())
l = [2*x for x in list(map(int, input().split()))]
for x in l:
    c[x] += 1

s = sum(l)
a = [(s-x)//2 for x in l]

count = 0
ans = []
for i in range(n):
    if a[i] in c:
        if (a[i] == l[i] and c[a[i]] > 1) or (a[i] != l[i]):
            count += 1
            ans.append(str(i+1))
print(count)
print(' '.join(ans))