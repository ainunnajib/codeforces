s = int(input())
a, b, c = map(int, input().split())
if a == 0 and b == 0 and c == 0:
    print(0, 0, 0)
else:
    x = 1.0*a*s/(a+b+c)
    y = 1.0*b*s/(a+b+c)
    z = 1.0*c*s/(a+b+c)
    print(x, y, z)