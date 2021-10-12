n, k = map(int, input().split())
if n%2 == 0:
    x = n//2
else:
    x = n//2 + 1

if k <= x:
    print(2*k-1)
else:
    print(2*(k-x))
