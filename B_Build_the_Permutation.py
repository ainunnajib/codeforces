t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    l = []
    if abs(a-b) > 1 or a+b > n-2:
        print(-1)
    else:
        if a == b:
            l.append(1)
            for i in range(1, a+1):
                l.append(2*i+1)
                l.append(2*i)
            for i in range(2*(a+1), n+1):
                l.append(i)
        elif a > b:
            for i in range(n-2*a):
                l.append(i+1)
            x = n-2*a+1
            for i in range(a):
                l.append(x+1)
                l.append(x)
                x += 2
        else:
            for i in range(b):
                l.append(2*i+2)
                l.append(2*i+1)
            for i in range(2*b+1, n+1):
                l.append(i)
        print(*l)