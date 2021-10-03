n = int(input())
l = list(map(int, input().split()))
a = [[], [], []]
for i in range(n):
    a[l[i]-1].append(i+1)

x = min(len(a[0]), len(a[1]), len(a[2]))
print(x)
for i in range(x):
    print(a[0][i], a[1][i], a[2][i])
