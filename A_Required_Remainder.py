t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    a = (n//x)*x+y
    if a > n:
        a -= x
    print(a)