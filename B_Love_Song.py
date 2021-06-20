n, q = map(int, input().split())
s = input()
l = [ord(c)-96 for c in s]
ll = [0 for i in range(n)]
ll[0] = l[0]
for i in range(1, n):
    ll[i] = ll[i-1] + l[i]
for _ in range(q):
    a, b = map(int, input().split())
    if a > 1:
        print(ll[b-1]-ll[a-2])
    else:
        print(ll[b-1])