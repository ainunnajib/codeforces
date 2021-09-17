n = int(input())
l = list(map(int, input().split()))
a = [0 for i in range(n)]
for i in range(n):
    a[l[i]-1] = i+1
s = [str(x) for x in a]
print(' '.join(s))