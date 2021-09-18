n, k = map(int, input().split())
t = 4*60 - k
while 5*(n*(n+1))//2 > t:
    n -= 1
print(n)