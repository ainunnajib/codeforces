MODULO = 1000000007

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        a = 1
        for i in range(3, 2*n+1):
            a *= i
            a %= MODULO
        print(a)