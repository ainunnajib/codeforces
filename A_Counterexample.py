from math import gcd
l, r = map(int, input().split())
if l%2 == 0 and r > l+1:
    print(l, l+1, l+2)
elif l%2 == 1 and r > l+2:
    print(l+1, l+2, l+3)
elif l%2 == 1:
    if gcd(l, l+2) > 1:
        print(l, l+1, l+2)
    else:
        print(-1)
else:
    print(-1)